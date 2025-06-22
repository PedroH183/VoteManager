from app.infra.db.database import Base
from app.domain.entities.topics_entity import Topic as TopicEntity

from sqlalchemy.orm import relationship, mapped_column, Mapped


class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)

    session = relationship("Session", back_populates="topic", cascade="all, delete-orphan")

    def to_dict(self) -> dict:
        """Converts the ORM model to a dictionary representation.

        Returns:
            dict: A dictionary containing the topic's id and title.
        """
        return {
            "id": self.id,
            "title": self.title,
        }

    def to_domain(self) -> TopicEntity:
        """Converts the ORM model to a domain entity.

        Returns:
            TopicEntity: An instance of TopicEntity representing the topic.
        """

        return TopicEntity(
            id_=self.id,
            title=self.title
        )
