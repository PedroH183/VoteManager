from typing import Protocol
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.session_entity import Session as DomainSession


class SessionRepository(Protocol):

    async def create(
        self, session: DomainSession, db_session: AsyncSession
    ) -> DomainSession:
        """This method creates a new session and persists it in the database.

        Args:
            session (DomainSession): A DomainSession object containing the session details.
            db_session (AsyncSession): An active database session for executing the operation.

        Returns:
            DomainSession: The created session entity persisted in the database.
        """
        ...
