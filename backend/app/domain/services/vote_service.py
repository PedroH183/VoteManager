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
        return await self._repo.vote(vote)

    async def get_by_user_and_session(self, user_id: int, session_id: int) -> DomainVote | None:
        """This method retrieves a vote by user ID and session ID.

        Args:
            user_id (int): The ID of the user who cast the vote.
            session_id (int): The ID of the session in which the vote was cast.

        Returns:
            DomainVote | None: The vote entity if found, otherwise None.
        """
        return await self._repo.get_by_user_and_session(user_id, session_id)