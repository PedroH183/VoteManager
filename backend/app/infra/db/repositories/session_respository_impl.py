from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infra.db.models.session_model import Session as ORMSession
from app.domain.entities.session_entity import Session as DomainSession
from app.application.protocols.session_repository import SessionRepository


class SessionRepositoryImpl(SessionRepository):
    def __init__(self, db_session: AsyncSession):
        self._db: AsyncSession = db_session

    async def create(self, session: DomainSession) -> DomainSession:
        """This method creates a new session for a specific topic and persists it in the database.

        Args:
            session (DomainSession): A DomainSession object containing the session details.

        Returns:
            DomainSession: The created session entity persisted in the database.
        """

        orm_obj = ORMSession(
            topic_id=session.topic_id,
            end_time=session.end_time,
            start_time=session.start_time,
        )
        self._db.add(orm_obj)
        await self._db.commit()
        await self._db.refresh(orm_obj)

        return orm_obj.to_domain()

    async def list(self) -> list[DomainSession]:
        """Return all sessions stored in the database."""

        result = await self._db.execute(select(ORMSession))
        orm_sessions = result.scalars().all()
        return [s.to_domain() for s in orm_sessions]

    async def get_by_id(self, session_id: int) -> DomainSession:
        """This method retrieves a session by its ID.

        Args:
            session_id (int): The ID of the session to retrieve.

        Returns:
            DomainSession: The session entity if found, otherwise raises ValueError.
        """
        result = await self._db.execute(
            select(ORMSession).where(ORMSession.id == session_id)
        )
        orm_user = result.scalars().first()

        if not orm_user:
            raise ValueError(f"Session with id {session_id} not found")
        return orm_user.to_domain()

    async def get_by_topic_id(self, topic_id: int) -> DomainSession:
        """Retrieve the latest session associated with a topic."""

        result = await self._db.execute(
            select(ORMSession)
            .where(ORMSession.topic_id == topic_id)
            .order_by(ORMSession.id.desc())
            .limit(1)
        )
        orm_session = result.scalars().first()
        if not orm_session:
            raise ValueError(f"Session for topic {topic_id} not found")
        return orm_session.to_domain()
