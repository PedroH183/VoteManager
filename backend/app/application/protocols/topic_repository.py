from typing import Protocol
from app.domain.entities.topics_entity import Topic as TopicDomain


class TopicRepository(Protocol):

    async def create(self, topic: TopicDomain) -> TopicDomain:
        """This method creates a new topic and persists it in the database.

        Args:
            topic (TopicDomain): A TopicDomain object containing the topic details.
            db_session (AsyncSession): An active database session for executing the operation.

        Returns:
            TopicDomain: The created topic entity persisted in the database.
        """
        ...

    async def list(self) -> list[TopicDomain]:
        """This method retrieves all topics from the database.

        Args:
            db_session (AsyncSession): An active database session for executing the operation.

        Returns:
            list[TopicDomain]: A list of DomainTopic entities representing all topics in the database.
        """
        ...
