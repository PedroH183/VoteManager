from app.infra.db.database import Base

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship, mapped_column, Mapped

from datetime import datetime

from app.domain.entities.session_entity import Session as DomainSession


class Session(Base):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(primary_key=True)
    end_time: Mapped[datetime] = mapped_column(nullable=False)

    start_time: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"), nullable=False)
    topic = relationship("Topic", back_populates="session")

    def to_dict(self) -> dict:
        """Returning a dictionary representation of the session"""
        return {
            "id": self.id,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "topic_id": self.topic_id,
            "durantion_time": (self.end_time - self.start_time).total_seconds() / 60 # type: ignore
        }

    def to_session(self) -> DomainSession:
        """Returning a session object from the ORM model"""
        return DomainSession(
            id_=self.id,
            start_time=self.start_time,
            topic_id=self.topic_id,
            duration_minutes=(self.end_time - self.start_time).total_seconds() / 60 # type: ignore
        )