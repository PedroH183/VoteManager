from typing import Optional, Protocol
from app.domain.entities.user_entity import User as DomainUser


class UserRepository(Protocol):
    async def create(self, user: DomainUser) -> DomainUser:
        """This method creates a new User and persists it in the database.

        Args:
            user (DomainUser): A DomainUser object containing the User details.

        Returns:
            DomainUser: The created User entity persisted in the database.
        """
        ...

    async def get_by_cpf(self, user_cpf: str) -> Optional[DomainUser]:
        """This method retrieves a user by its CPF.

        Args:
            user_cpf (str): The CPF of the user to retrieve.

        Returns:
            Optional[DomainUser]: The user entity if found, otherwise None.
        """
        ...