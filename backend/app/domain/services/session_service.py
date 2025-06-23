from app.domain.entities.session_entity import Session as DomainSession
from app.application.protocols.session_repository import SessionRepository


class SessionService:
    """Service to manage session operations."""

    def __init__(self, repo: SessionRepository):
        self._repo = repo

    async def open_session(self, session: DomainSession) -> DomainSession:
        """This method creates a new session for a specific topic and persists it in the database.

        Args:
            session (DomainSession): A DomainSession object containing the session details.
            db_session (AsyncSession): An asynchronous database session for database operations.

        Returns:
            DomainSession: The created session entity persisted in the database.
        """

        domain_sess = DomainSession(
            session.topic_id, duration_minutes=session.duration_time
        )
        return await self._repo.create(domain_sess)

    async def list(self) -> list[DomainSession]:
        """Return all sessions."""

        return await self._repo.list()

    async def get_by_id(self, session_id: int) -> DomainSession:
        """This method retrieves a session by its ID.

        Args:
            session_id (int): The ID of the session to retrieve.

        Returns:
            DomainSession: The session entity if found, otherwise raises ValueError.
        """
        return await self._repo.get_by_id(session_id)

    async def get_by_topic_id(self, topic_id: int) -> DomainSession:
        """Retrieve a session associated with a given topic."""

        return await self._repo.get_by_topic_id(topic_id)
