from app.infra.db.database import Base
from app.domain.entities.user_entity import User as UserEntity

from sqlalchemy.orm import relationship, mapped_column, Mapped


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(nullable=False)
    cpf: Mapped[str] = mapped_column(nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(nullable=False)

    votes = relationship("Vote", back_populates="user")

    def to_domain(self) -> UserEntity:
        """Converts the ORM model to a domain entity.

        Returns:
            VoteEntity: An instance of VoteEntity representing the vote.
        """
        return UserEntity(
            id_=self.id, name=self.name, cpf=self.cpf, password=self.password_hash
        )
