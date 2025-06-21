from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.infra.db.database import get_db
from app.domain.services.topic_service import TopicService
from app.api.schemas.topic_schemas import TopicCreateDTO, TopicResponseDTO
from app.domain.entities.topics_entity import Topic as DomainTopic
from app.application.protocols.topic_repository import TopicRepository
from app.infra.db.repositories.topic_repository_impl import TopicRepositoryImpl


router = APIRouter(prefix="/topics", tags=["Topics"])


# TODO ADD USER DEPENDENCY IN create_topic
@router.post("", response_model=TopicResponseDTO, status_code=status.HTTP_201_CREATED)
async def create_topic(
    payload: TopicCreateDTO,
    db: AsyncSession = Depends(get_db),
):
    """
    This endpoint allows the creation of a new topic that can be used in a voting session.

    Args:
        payload (TopicCreateDTO): _description_
        db (AsyncSession, optional): _description_. Defaults to Depends(get_db).

    Returns:
        _type_: _description_
    """
    repo: TopicRepository = TopicRepositoryImpl(db)
    service = TopicService(repo)

    domain_session = DomainTopic(
        title=payload.title,
    )
    created = await service.create(domain_session, db)
    return TopicResponseDTO.from_domain(created)


@router.post("", response_model=List[TopicResponseDTO], status_code=status.HTTP_200_OK)
async def list_topics(db: AsyncSession = Depends(get_db)):
    """
    This endpoint retrieves a list of all topics available in the system.

    Args:
        db (AsyncSession, optional): Database session dependency. Defaults to Depends(get_db).

    Returns:
        List[TopicResponseDTO]: A list of topics available in the system.
    """
    return await TopicService(TopicRepositoryImpl(db)).list(db)
