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
