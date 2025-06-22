from fastapi import APIRouter, Depends, status

from app.domain.services.session_service import SessionService
from app.api.schemas.session_schemas import SessionCreateDTO, SessionResponseDTO
from app.domain.entities.session_entity import Session as DomainSession
from app.api.deps import get_session_service



router = APIRouter(prefix="/topics/{topic_id}/session", tags=["Sessions"])


# TODO ADD USER DEPENDENCY IN OPEN SESSION
@router.post("", response_model=SessionResponseDTO, status_code=status.HTTP_201_CREATED)
async def open_session(
    topic_id: int,
    payload: SessionCreateDTO,
    session_service: SessionService = Depends(get_session_service),
):
    """This endpoint allows the creation of a new session for a specific topic.

    Args:
        topic_id (int): The ID of the topic for which the session is being created.
        payload (SessionCreateDTO): The data containing the session details

    Returns:
        SessionResponseDTO: A response containing the details of the created session.
    """

    domain_session = DomainSession(
        topic_id=topic_id,
        duration_minutes=payload.duration_minutes or 1,
    )
    created = await session_service.open_session(domain_session)
    return SessionResponseDTO.from_domain(created)
