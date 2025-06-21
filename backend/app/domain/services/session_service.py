from app.domain.entities.session_entity import Session as DomainSession
from app.application.protocols.session_repository import SessionRepository

from sqlalchemy.ext.asyncio import AsyncSession


class SessionService:
    """Service to manage session operations."""

    def __init__(self, repo: SessionRepository):
        self._repo = repo

    async def open_session(
        self, session: DomainSession, db_session: AsyncSession
    ) -> DomainSession:
        """Opens a new voting session for a topic."""

        domain_sess = DomainSession(
            session.topic_id, duration_minutes=session.duration_time
        )
        return await self._repo.create(domain_sess, db_session)
