from typing import Protocol
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.session_entity import Session as DomainSession


class SessionRepository(Protocol):
    
    async def create(
        self, session: DomainSession, db_session: AsyncSession
    ) -> DomainSession:
        """Persiste uma nova sessão e retorna a entidade criada."""
        
        from app.infra.db.repositories.session_respository_impl import SessionRepositoryImpl

        _session_repository: SessionRepositoryImpl = SessionRepositoryImpl(db_session)
        return await _session_repository.create(session)
