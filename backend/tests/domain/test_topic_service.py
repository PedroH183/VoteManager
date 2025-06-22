import asyncio

from app.domain.entities.topics_entity import Topic
from app.domain.services.topic_service import TopicService


class FakeTopicRepo:
    def __init__(self):
        self.topics = []
        self._id = 1

    async def create(self, topic: Topic) -> Topic:
        topic = Topic(id_=self._id, title=topic.title)
        self._id += 1
        self.topics.append(topic)
        return topic

    async def list(self) -> list[Topic]:
        return list(self.topics)

    async def get(self, topic_id: int) -> Topic:
        for t in self.topics:
            if t.id == topic_id:
                return t
        raise ValueError(f"Topic with id {topic_id} not found")


def test_topic_service_create_and_list():
    repo = FakeTopicRepo()
    service = TopicService(repo)
    created = asyncio.run(service.create(Topic(title="My Topic")))

    assert created.id == 1
    assert created.title == "My Topic"

    topics = asyncio.run(service.list())
    assert len(topics) == 1
    assert topics[0].title == "My Topic"


def test_topic_service_get():
    repo = FakeTopicRepo()
    service = TopicService(repo)
    created = asyncio.run(service.create(Topic(title="Another")))

    fetched = asyncio.run(service.get(created.id))
    assert fetched.id == created.id
    assert fetched.title == "Another"
