import enum

from sqlalchemy import ForeignKey, Enum
from app.infra.db.database import Base
from app.domain.entities.vote_entity import Vote as VoteEntity

from sqlalchemy.orm import relationship, mapped_column, Mapped


class VoteOption(str, enum.Enum):
    SIM = "Sim"
    NAO = "Não"


class Vote(Base):
    __tablename__ = "votes"

    id: Mapped[int] = mapped_column(primary_key=True)

    option: Mapped[VoteOption] = mapped_column(
        Enum(VoteOption), name="vote_option", nullable=False
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user = relationship("User", back_populates="votes")

    session_id: Mapped[int] = mapped_column(ForeignKey("sessions.id"))
    session = relationship("Session", back_populates="votes")

    def to_domain(self) -> VoteEntity:
        """Converts the ORM model to a domain entity.

        Returns:
            VoteEntity: An instance of VoteEntity representing the vote.
        """
        return VoteEntity(
            id_=self.id,
            user_id=self.user_id,
            option=self.option.value,
            session_id=self.session_id,
        )
