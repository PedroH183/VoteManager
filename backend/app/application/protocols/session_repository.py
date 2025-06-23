from typing import Protocol
from app.domain.entities.session_entity import Session as DomainSession


class SessionRepository(Protocol):

    async def create(self, session: DomainSession) -> DomainSession:
        """This method creates a new session and persists it in the database.

        Args:
            session (DomainSession): A DomainSession object containing the session details.
            db_session (AsyncSession): An active database session for executing the operation.

        Returns:
            DomainSession: The created session entity persisted in the database.
        """
        ...

    async def list(self) -> list[DomainSession]:
        """Retrieve all sessions stored in the repository."""
        ...

    async def get_by_topic_id(self, topic_id: int) -> DomainSession:
        """Retrieve a session by the associated topic ID.

        Args:
            topic_id (int): The ID of the topic linked to the session.

        Returns:
            DomainSession: The session entity if found, otherwise raises
                ``ValueError``.
        """
        ...

    async def get_by_id(self, session_id: int) -> DomainSession:
        """This method retrieves a session by its ID.

        Args:
            session_id (int): The ID of the session to retrieve.

        Returns:
            DomainSession: The session entity if found, otherwise raises ValueError.
        """
        ...