from typing import Optional
from pydantic import BaseModel, Field

from app.domain.entities.topics_entity import Topic as DomainTopic


class TopicCreateDTO( BaseModel ):
    title: str = Field(
        ...,
        title="Title",
        description="Title of the topic for the voting session",
    )


class TopicResponseDTO( BaseModel ):
    id: Optional[int] = Field(..., title="Topic ID")
    title: str = Field(..., title="Topic Title")

    @classmethod
    def from_domain(cls, topic: DomainTopic) -> "TopicResponseDTO":
        return cls(
            id=topic.id,
            title=topic.title,
        )

    class Config:
        from_attributes = True
