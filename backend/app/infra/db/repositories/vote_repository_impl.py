from sqlalchemy.ext.asyncio import AsyncSession

from app.infra.db.models.vote_model import Vote as ORMVote
from app.domain.entities.vote_entity import Vote as DomainVote
from app.application.protocols.vote_repository import VoteRepository


class VoteRepositoryImpl(VoteRepository):
    
    def __init__(self, db_session: AsyncSession):
        self._db: AsyncSession = db_session

    async def vote(self, vote: DomainVote) -> DomainVote:
        """This method creates a new vote in the database.

        Args:
            vote (DomainVote): A DomainVote entity representing the vote to be created.

        Returns:
            DomainVote: A DomainVote entity representing the created vote.
        """
        orm_obj = ORMVote(
            option=vote.option,
            session_id=vote.session_id,
        )
        self._db.add(orm_obj)

        await self._db.commit()
        await self._db.refresh(orm_obj)

        return orm_obj.to_domain()

