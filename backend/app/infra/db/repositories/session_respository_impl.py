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
            topic_id  = session.topic_id,
            end_time  = session.end_time,
            start_time= session.start_time,
        )
        self._db.add(orm_obj)
        await self._db.commit()
        await self._db.refresh(orm_obj)

        return orm_obj.to_domain()

