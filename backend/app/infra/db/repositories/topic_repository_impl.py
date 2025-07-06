from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models.topic_model import Topic as ORMTopic
from app.domain.entities.topics_entity import Topic as DomainTopic
from app.application.protocols.topic_repository import TopicRepository


class TopicRepositoryImpl(TopicRepository):
    def __init__(self, db_session: AsyncSession):
        self._db: AsyncSession = db_session

    async def create(self, topic: DomainTopic) -> DomainTopic:
        """This method creates a new topic and persists it in the database.

        Args:
            topic (DomainTopic): A DomainTopic object containing the topic details.
        Returns:
            DomainTopic: The created topic entity persisted in the database.
        """
        orm_obj = ORMTopic(
            title=topic.title,
        )
        self._db.add(orm_obj)

        await self._db.commit()
        await self._db.refresh(orm_obj)

        return orm_obj.to_domain()

    async def list(self) -> list[DomainTopic]:
        """This method retrieves all topics from the database.

        Returns:
            list[DomainTopic]: A list of DomainTopic entities representing all topics in the database.
        """

        result = await self._db.execute(select(ORMTopic).order_by(ORMTopic.id.desc()))
        orm_topic = result.scalars().all()

        return [orm_session.to_domain() for orm_session in orm_topic]
    

    async def get(self, topic_id: int) -> DomainTopic:
        """This method retrieves a topic by its ID.

        Args:
            topic_id (int): The ID of the topic to retrieve.

        Returns:
            DomainTopic: The topic entity with the specified ID.
        """
        result = await self._db.execute(select(ORMTopic).where(ORMTopic.id == topic_id))
        orm_topic = result.scalar_one_or_none()

        if orm_topic is None:
            raise ValueError(f"Topic with id {topic_id} not found")

        return orm_topic.to_domain()
