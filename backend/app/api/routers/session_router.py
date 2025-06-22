from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps_auth import get_current_user
from app.domain.services.session_service import SessionService
from app.api.schemas.session_schemas import SessionCreateDTO, SessionResponseDTO
from app.domain.entities.session_entity import Session as DomainSession
from app.api.deps import get_session_service, get_topic_service
from app.domain.services.topic_service import TopicService


router = APIRouter(prefix="/topics/{topic_id}/session", tags=["Sessions"])


@router.post(
    "",
    summary="Open a new voting session",
    description="Open a voting session for a given topic. Optionally specify duration in minutes (default is 1 minute).",
    response_model=SessionResponseDTO,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_current_user)],
    responses={
        400: {"description": "Bad Request: invalid payload or session already exists"},
        401: {"description": "Unauthorized: invalid or missing token"},
        404: {"description": "Topic not found"},
    },
)
async def open_session(
    topic_id: int,
    payload: SessionCreateDTO,
    session_service: SessionService = Depends(get_session_service),
    topic_service: TopicService = Depends(get_topic_service),
):
    """This endpoint allows the creation of a new session for a specific topic.

    Args:
        topic_id (int): The ID of the topic for which the session is being created.
        payload (SessionCreateDTO): The data containing the session details

    Returns:
        SessionResponseDTO: A response containing the details of the created session.
    """

    try:
        await topic_service.get(topic_id)
    except ValueError:
        raise HTTPException(
            detail="Topic not found !!",
            status_code=status.HTTP_404_NOT_FOUND
        )

    domain_session = DomainSession(
        topic_id=topic_id,
        duration_minutes=payload.duration_minutes or 1,
    )
    created = await session_service.open_session(domain_session)
    return SessionResponseDTO.from_domain(created)
