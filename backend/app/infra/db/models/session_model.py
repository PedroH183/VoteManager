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

    topic_id: Mapped[int] = mapped_column(
        ForeignKey("topics.id", ondelete="cascade"), nullable=False
    )
    topic = relationship("Topic", back_populates="session")
    
    votes = relationship(
        "Vote", back_populates="session", cascade="all, delete-orphan"
    )

    def to_domain(self) -> DomainSession:
        """This method converts the ORM model to a domain entity.

        Returns:
            DomainSession: An instance of DomainSession representing the session.
        """
        return DomainSession(
            id_=self.id,
            topic_id=self.topic_id,
            start_time=self.start_time,
            duration_minutes=(self.end_time - self.start_time).total_seconds() / 60,  # type: ignore
        )
