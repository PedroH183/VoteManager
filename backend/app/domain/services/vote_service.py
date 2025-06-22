from app.domain.entities.vote_entity import Vote as DomainVote
from app.application.protocols.vote_repository import VoteRepository


class VoteService:
    """Topic service to manage topic-related operations."""

    def __init__(self, repo: VoteRepository):
        self._repo = repo

    async def vote(self, vote: DomainVote) -> DomainVote:
        """This method creates a new vote and persists it in the database.

        Args:
            vote (DomainVote): A DomainVote object containing the vote details.
            db_session (AsyncSession): An asynchronous database session for database operations.

        Returns:
            DomainVote: The created vote entity persisted in the database.
        """
        # TODO: VALIDATE IF TOPIC EXISTS
        # TODO: VALIDATE IF USER ALREADY VOTED ON THIS TOPIC
        # TODO; VALIDATE IF SESSION IS ACTIVE


        return await self._repo.vote(vote)

