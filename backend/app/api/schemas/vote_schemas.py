from typing import Optional, ClassVar, Set
from pydantic import BaseModel, Field, field_validator

from app.domain.entities.vote_entity import Vote as DomainVote


class VoteCreateDTO(BaseModel):
    session_id: int = Field(
        ...,
        title="Session ID",
        description="ID of the session associated with the vote",
    )
    option: str = Field(
        ...,
        title="Vote Option",
        description="The option selected in the vote, e.g., 'Sim' or 'Não'",
    )

    _valid_options: ClassVar[Set[str]] = {"Sim", "Não"}

    @field_validator("option")
    def check_option(cls, v: str) -> str:
        if v not in cls._valid_options:
            raise ValueError(f"option must be one of {cls._valid_options!r}")
        return v


class VoteResponseDTO(BaseModel):
    
    id: Optional[int] = Field(..., title="Vote ID")
    session_id: Optional[int] = Field(..., title="Session ID")
    option: str = Field(..., title="Vote Option")

    @classmethod
    def from_domain(cls, Vote: DomainVote) -> "VoteResponseDTO":
        return cls(
            id=Vote.id,
            option=Vote.option,
            session_id=Vote.session_id
        )

    class Config:
        from_attributes = True
