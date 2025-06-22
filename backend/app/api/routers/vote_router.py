from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps_auth import get_current_user
from app.domain.entities.user_entity import User as DomainUser
from app.domain.services.session_service import SessionService
from app.domain.services.vote_service import VoteService
from app.domain.entities.vote_entity import Vote as DomainVote
from app.api.schemas.vote_schemas import VoteCreateDTO, VoteResponseDTO

from app.api.deps import get_session_service, get_vote_service

router = APIRouter(prefix="/topics/{topic_id}/vote", tags=["Vote"])


@router.post(
    "",
    summary="Cast a vote in a session",
    description="Allows an authenticated user to cast a vote ('Sim' or 'Não') in a specific voting session.",
    response_model=VoteResponseDTO,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Bad Request: payload mismatch or validation error"},
        401: {"description": "Unauthorized: invalid or missing token"},
        404: {"description": "Session not found"},
        409: {"description": "Conflict: user has already voted in this session"},
    },
)
async def vote(
    payload: VoteCreateDTO,
    current_user: DomainUser = Depends(get_current_user),
    vote_service: VoteService = Depends(get_vote_service),
    session_service: SessionService = Depends(get_session_service),
):
    """This endpoint allows a user to cast a vote on a specific topic in a voting session.

    Args:
        payload (VoteCreateDTO): VoteData to be created, which includes the vote option and topic ID.
        db (AsyncSession, optional): Database session dependency. Defaults to Depends(get_db).

    Returns:
        _VoteResponseDTO_: A VoteResponseDTO containing the details of the created vote.
    """
    try:
        session = await session_service.get_by_id(payload.session_id)
    except ValueError as e:
        raise HTTPException(
            detail=str(e),
            status_code=status.HTTP_404_NOT_FOUND,
        )

    # Check if the session stil is open for voting
    if not session.is_open:
        raise HTTPException(
            detail="Session is not open for voting",
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    # Check if the user has already voted in this session
    if await vote_service.get_by_user_and_session(
        current_user.id, session_id=payload.session_id # type: ignore
    ):
        raise HTTPException(
            detail="User has already voted in this session",
            status_code=status.HTTP_409_CONFLICT,
        )

    domain_session = DomainVote(
        option=payload.option,
        user_id=current_user.id,  # type: ignore
        session_id=payload.session_id,
    )
    created = await vote_service.vote(domain_session)
    return VoteResponseDTO.from_domain(created)
