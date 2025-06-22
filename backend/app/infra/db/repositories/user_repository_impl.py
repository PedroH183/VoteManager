from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infra.db.models.user_model import User as ORMUser
from app.domain.entities.user_entity import User as DomainUser
from app.application.protocols.user_repository import UserRepository

from app.infra.auth.hashing import get_password_hash


class UserRepositoryImpl(UserRepository):
    def __init__(self, db_session: AsyncSession):
        self._db: AsyncSession = db_session

    async def create(self, user: DomainUser) -> DomainUser:
        """This method creates a new user and persists it in the database.

        Args:
            user (DomaiDomainUsernTopic): A DomainUser object containing the user details.
        Returns:
            DomainUser: The created user entity persisted in the database.
        """
        orm_obj = ORMUser(
            cpf=user.cpf,
            name=user.name,
            password_hash=get_password_hash(user.password),
        )
        self._db.add(orm_obj)

        await self._db.commit()
        await self._db.refresh(orm_obj)

        return orm_obj.to_domain()

    async def get_by_cpf(self, cpf: str) -> Optional[DomainUser]:
        """This method retrieves a user by their CPF from the database.

        Args:
            cpf (str): The CPF of the user to retrieve.

        Returns:
            DomainUser | None: The user entity if found, otherwise None.
        """
        result = await self._db.execute(select(ORMUser).where(ORMUser.cpf == cpf))
        orm_user = result.scalars().first()

        if orm_user is None:
            raise ValueError(f"User with cpf {cpf} not found")

        return orm_user.to_domain()

    async def get_by_id(self, user_id: int) -> Optional[DomainUser]:
        """This method retrieves a user by their ID from the database.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            Optional[DomainUser]: The user entity if found, otherwise None.
        """
        result = await self._db.execute(select(ORMUser).where(ORMUser.id == user_id))
        orm_user = result.scalars().first()

        if orm_user is None:
            raise ValueError(f"User with id {user_id} not found")

        return orm_user.to_domain() if orm_user else None
