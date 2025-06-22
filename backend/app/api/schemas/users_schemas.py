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

    class Config:
        from_attributes = True


class UserCreate(User):
    password: str = Field(..., title="Password of the user", min_length=6)


class UserResponse(User):
    id: Optional[int] = Field(None, title="ID of the user")

    @classmethod
    def from_domain(cls, user) -> "UserResponse":
        return cls(
            id=user.id or None,
            cpf=user.cpf,
            name=user.name,
        )


class UserInDB(User):
    hashed_password: str
