from typing import List
from fastapi import APIRouter, Depends, status

from app.api.deps_auth import get_current_user
from app.domain.services.topic_service import TopicService
from app.api.schemas.topic_schemas import TopicCreateDTO, TopicResponseDTO
from app.domain.entities.topics_entity import Topic as DomainTopic


from app.api.deps import get_topic_service

router = APIRouter(prefix="/topics", tags=["Topics"])


@router.post(
    "",
    summary="Create a new topic",
    description="Allows an authenticated user to create a new voting topic in the system.",
    response_model=TopicResponseDTO,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_current_user)],
    responses={
        400: {"description": "Bad Request: invalid payload"},
        401: {"description": "Unauthorized: missing or invalid token"}
    }
)
async def create_topic(
    payload: TopicCreateDTO, 
    topic_service: TopicService = Depends(get_topic_service),
):
    """
    This endpoint allows the creation of a new topic that can be used in a voting session.

    Args:
        payload (TopicCreateDTO): _description_
        db (AsyncSession, optional): _description_. Defaults to Depends(get_db).

    Returns:
        _type_: _description_
    """

    domain_session = DomainTopic(
        title=payload.title,
    )
    created = await topic_service.create(domain_session)
    return TopicResponseDTO.from_domain(created)


@router.get(
    "",
    summary="List all topics",
    description="Retrieve a list of all voting topics available in the system.",
    response_model=List[TopicResponseDTO],
    status_code=status.HTTP_200_OK
)
async def list_topics(topic_service: TopicService = Depends(get_topic_service)):
    """
    This endpoint retrieves a list of all topics available in the system.

    Args:
        db (AsyncSession, optional): Database session dependency. Defaults to Depends(get_db).

    Returns:
        List[TopicResponseDTO]: A list of topics available in the system.
    """
    return await topic_service.list()
