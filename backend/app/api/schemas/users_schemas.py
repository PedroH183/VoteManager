from typing import Optional
from pydantic import BaseModel, Field
from app.domain.entities.user_entity import User as DomainUser


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    cpf: str


class User(BaseModel):
    cpf: str = Field(..., title="CPF of the user")
    name: str = Field(..., title="Username of the user")
    password: str = Field(..., title="Password of the user")

    @classmethod
    def from_domain(cls, user: DomainUser) -> "User":
        return cls(
            cpf=user.cpf,
            name=user.name,
            password=user.password
        )

    class Config:
        from_attributes = True


class UserInDB(User):
    hashed_password: str
