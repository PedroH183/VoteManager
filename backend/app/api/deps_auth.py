import jwt
import os
from dotenv import load_dotenv
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.infra.db.database import get_db
from app.domain.services.user_service import UserService
from app.domain.entities.user_entity import User as UserDomain
from app.infra.db.repositories.user_repository_impl import UserRepositoryImpl


load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(UserRepositoryImpl(db))


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    user_service: UserService = Depends(get_user_service),
) -> UserDomain | None:
    """This function retrieves the jwt token from the request and decodes
    it to get the user information.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user_not_found_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            os.getenv("SECRET_KEY"),
            algorithms=[os.getenv("ALGORITHM", "HS256")],
        )
    except jwt.InvalidTokenError:
        raise credentials_exception
    
    cpf = payload.get("sub", None)
    if cpf is None:
        raise credentials_exception

    try:
        user = await user_service.get_by_cpf(cpf=cpf)
    except ValueError:
        raise user_not_found_exception

    return user
