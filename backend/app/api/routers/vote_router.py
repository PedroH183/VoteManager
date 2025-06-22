from fastapi import APIRouter, Depends, status

from app.domain.services.vote_service import VoteService
from app.domain.entities.vote_entity import Vote as DomainVote
from app.api.schemas.vote_schemas import VoteCreateDTO, VoteResponseDTO

from app.api.deps import get_vote_service

router = APIRouter(prefix="/topics/{topic_id}/vote", tags=["Vote"])


# TODO ADD USER DEPENDENCY IN create_topic
@router.post("", response_model=VoteCreateDTO, status_code=status.HTTP_201_CREATED)
async def vote(
    payload: VoteCreateDTO,
    vote_service: VoteService = Depends(get_vote_service),
):
    """This endpoint allows a user to cast a vote on a specific topic in a voting session.

    Args:
        payload (VoteCreateDTO): VoteData to be created, which includes the vote option and topic ID.
        db (AsyncSession, optional): Database session dependency. Defaults to Depends(get_db).

    Returns:
        _VoteResponseDTO_: A VoteResponseDTO containing the details of the created vote.
    """

    domain_session = DomainVote(
        option= payload.option,
        session_id=payload.session_id
    )
    created = await vote_service.vote(domain_session)
    return VoteResponseDTO.from_domain(created)
