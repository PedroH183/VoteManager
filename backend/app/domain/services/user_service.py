from typing import Optional
from app.domain.entities.user_entity import User as DomainUser
from app.application.protocols.user_repository import UserRepository


class UserService:
    """USer service to manage user-related operations."""

    def __init__(self, repo: UserRepository):
        self._repo = repo

    async def create(self, user: DomainUser) -> DomainUser:
        """This method creates a new user and persists it in the database.

        Args:
            user (DomainUser): A DomainUser object containing the topic details.
            db_session (AsyncSession): An asynchronous database session for database operations.

        Returns:
            DomainTopic: The created topic entity persisted in the database.
        """

        domain_user = DomainUser(cpf=user.cpf, name=user.name, password=user.password)
        return await self._repo.create(domain_user)

    async def get_by_cpf(self, cpf: str) -> Optional[DomainUser]:
        """This method retrieves a user by their CPF.

        Args:
            cpf (str): The CPF of the user to retrieve.

        Returns:
            DomainUser | None: The user entity if found, otherwise None.
        """
        return await self._repo.get_by_cpf(cpf)