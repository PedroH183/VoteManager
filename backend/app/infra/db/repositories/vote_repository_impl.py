from sqlalchemy import select
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
            user_id=vote.user_id,
            session_id=vote.session_id,
        )
        self._db.add(orm_obj)

        await self._db.commit()
        await self._db.refresh(orm_obj)

        return orm_obj.to_domain()

    async def get_by_user_and_session(
        self, user_id: int, session_id: int
    ) -> DomainVote | None:
        """This method retrieves a vote by user ID and session ID.

        Args:
            user_id (int): The ID of the user who cast the vote.
            session_id (int): The ID of the session in which the vote was cast.

        Returns:
            DomainVote | None: The vote entity if found, otherwise None.
        """

        result = await self._db.execute(
            select(ORMVote)
            .filter(ORMVote.user_id == user_id, ORMVote.session_id == session_id)
            .limit(1)
        )
        orm_obj = result.scalars().first()
        return orm_obj.to_domain() if orm_obj else None
