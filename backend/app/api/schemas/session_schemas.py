from typing import Optional
from pydantic import BaseModel, Field

from app.domain.entities.session_entity import Session as DomainSession


class SessionCreateDTO(BaseModel ):
    duration_minutes: Optional[int] = Field(
        1,
        title="Session Duration",
        description="Duration of the voting session in minutes (default=1)",
        ge=1,
    )


class SessionResponseDTO(BaseModel):
    id: Optional[int] = Field(..., title="Session ID")
    topic_id: int = Field(..., title="Topic ID")
    
    end_time: str = Field(..., title="Session End Time")
    start_time: str = Field(..., title="Session Start Time")

    duration_minutes: int = Field(..., title="Duration in Minutes")

    @classmethod
    def from_domain(cls, session: DomainSession) -> "SessionResponseDTO":
        return cls(
            id=session.id,
            topic_id=session.topic_id,
            end_time=session.end_time_str,
            start_time=session.start_time_str,
            duration_minutes=session.duration_time,
        )

    class Config:
        from_attributes = True
