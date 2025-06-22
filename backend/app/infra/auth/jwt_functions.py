import os
import jwt

from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv


from app.infra.auth.hashing import verify_password
from app.domain.services.user_service import UserService
from app.domain.entities.user_entity import User as UserDomain

load_dotenv()


async def authenticate_user(
    cpf: str, password: str, user_service: UserService
) -> UserDomain | None:
    user = await user_service.get_by_cpf(cpf)
    return user if user and verify_password(password, user.password) else None


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM")
    )
    return encoded_jwt
