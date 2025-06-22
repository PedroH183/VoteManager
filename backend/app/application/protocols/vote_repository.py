from typing import Protocol
from app.domain.entities.vote_entity import Vote as DomainVote


class VoteRepository(Protocol):
    async def vote(self, vote: DomainVote) -> DomainVote:
        """This method creates a new topic and persists it in the database.

        Args:
            topic (DomainTopic): A DomainTopic object containing the topic details.
            db_session (AsyncSession): An active database session for executing the operation.

        Returns:
            DomainTopic: The created topic entity persisted in the database.
        """
        ...

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
        ...

    async def count_by_session(self, session_id: int) -> dict[str, int]:
        """Return the number of votes for each option in a session.

        Args:
            session_id (int): The ID of the session to aggregate votes for.

        Returns:
            dict[str, int]: A mapping of vote option to vote count.
        """
        ...
