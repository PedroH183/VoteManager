from app.domain.entities.topics_entity import Topic as DomainTopic
from app.application.protocols.topic_repository import TopicRepository


class TopicService:
    """Topic service to manage topic-related operations."""

    def __init__(self, repo: TopicRepository):
        self._repo = repo

    async def create(self, topic: DomainTopic) -> DomainTopic:
        """This method creates a new topic and persists it in the database.

        Args:
            topic (DomainTopic): A DomainTopic object containing the topic details.
            db_session (AsyncSession): An asynchronous database session for database operations.

        Returns:
            DomainTopic: The created topic entity persisted in the database.
        """

        domain_topic = DomainTopic(title=topic.title)
        return await self._repo.create(domain_topic)

    async def list(self) -> list[DomainTopic]:
        """This method retrieves all topics from the database.

        Args:
            db_session (AsyncSession): A asynchronous database session for database operations.

        Returns:
            list[DomainTopic]: A list of DomainTopic entities representing all topics in the database.
        """
        return await self._repo.list()
    
    async def get(self, topic_id: int) -> DomainTopic:
        """This method retrieves a topic by its ID.

        Args:
            topic_id (int): The ID of the topic to retrieve.

        Returns:
            DomainTopic: The topic entity with the specified ID.
        """
        return await self._repo.get(topic_id)
