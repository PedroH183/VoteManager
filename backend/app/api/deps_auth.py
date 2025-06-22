import jwt
import os
from dotenv import load_dotenv
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.api.schemas.users_schemas import TokenData
from app.domain.services.user_service import UserService
from app.infra.db.database import get_db
from app.infra.db.repositories.user_repository_impl import UserRepositoryImpl


load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(UserRepositoryImpl(db))


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    user_service: UserService = Depends(get_user_service),
):
    """This function retrieves the jwt token from the request and decodes
    it to get the user information.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            os.getenv("SECRET_KEY"),
            algorithms=[os.getenv("ALGORITHM", "HS256")],
        )
        cpf = payload.get("sub")
        if cpf is None:
            raise credentials_exception

        token_data = TokenData(cpf=cpf)

    except jwt.InvalidTokenError:
        raise credentials_exception

    user = await user_service.get_by_cpf(cpf=token_data.cpf)

    if user is None:
        raise credentials_exception

    return user
