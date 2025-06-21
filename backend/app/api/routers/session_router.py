from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.infra.db.database import get_db
from app.domain.services.session_service import SessionService
from app.api.schemas.session_schemas import SessionCreate, SessionRead
from app.domain.entities.session_entity import Session as DomainSession
from app.application.protocols.session_repository import SessionRepository
from app.infra.db.repositories.session_respository_impl import SessionRepositoryImpl


router = APIRouter(prefix="/topics/{topic_id}/session", tags=["Sessions"])


# TODO ADD USER DEPENDENCY IN OPEN SESSION
@router.post("", response_model=SessionRead, status_code=status.HTTP_201_CREATED)
async def open_session(
    topic_id: int,
    payload: SessionCreate,
    db: AsyncSession = Depends(get_db),
):
    repo: SessionRepository = SessionRepositoryImpl(db)
    service = SessionService(repo)

    domain_session = DomainSession(
        topic_id=topic_id,
        start_time=payload.start_time,
        duration_minutes=payload.duration_minutes,
    )
    created = await service.open_session(domain_session, db)
    return SessionRead.from_domain(created)
