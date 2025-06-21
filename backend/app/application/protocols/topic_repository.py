from typing import Protocol
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.topics_entity import Topic as TopicDomain


class TopicRepository(Protocol):
    
    async def create(
        self, topic: TopicDomain, db_session: AsyncSession
    ) -> TopicDomain:
        """This method creates a new topic and persists it in the database.

        Args:
            topic (TopicDomain): A TopicDomain object containing the topic details.
            db_session (AsyncSession): An active database session for executing the operation.

        Returns:
            TopicDomain: The created topic entity persisted in the database.
        """
        
        from app.infra.db.repositories.topic_repository_impl import TopicRepositoryImpl

        _topic_repository: "TopicRepository" = TopicRepositoryImpl(db_session)
        return await _topic_repository.create(topic)

    async def list(self, db_session: AsyncSession) -> list[TopicDomain]:
        """This method retrieves all topics from the database.

        Args:
            db_session (AsyncSession): An active database session for executing the operation.

        Returns:
            list[TopicDomain]: A list of DomainTopic entities representing all topics in the database.
        """
        
        from app.infra.db.repositories.topic_repository_impl import TopicRepositoryImpl

        _topic_repository: "TopicRepository" = TopicRepositoryImpl(db_session)
        return await _topic_repository.list()