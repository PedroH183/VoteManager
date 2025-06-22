from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infra.db.database import get_db

from app.infra.db.repositories.session_respository_impl import SessionRepositoryImpl
from app.infra.db.repositories.vote_repository_impl import VoteRepositoryImpl
from app.infra.db.repositories.topic_repository_impl import TopicRepositoryImpl


from app.domain.services.session_service import SessionService
from app.domain.services.vote_service import VoteService
from app.domain.services.topic_service import TopicService


async def get_session_service(db: AsyncSession = Depends(get_db)) -> SessionService:
    return SessionService(SessionRepositoryImpl(db))

async def get_vote_service(db: AsyncSession = Depends(get_db)) -> VoteService:
    return VoteService(VoteRepositoryImpl(db))

async def get_topic_service(db: AsyncSession = Depends(get_db)) -> TopicService:
    return TopicService(TopicRepositoryImpl(db))