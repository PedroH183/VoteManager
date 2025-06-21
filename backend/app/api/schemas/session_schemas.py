from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

from app.domain.entities.session_entity import Session as DomainSession


class SessionCreateDTO(BaseModel ):
    topic_id: int = Field(
        ..., 
        title="Topic ID", 
        description="ID of the topic for which the session is created",
    ) 
    start_time: Optional[datetime] = Field(
        None,
        title="Session Start Time",
        description="Start time of the voting session (default is now)",
    )
    duration_minutes: Optional[int] = Field(
        1,
        title="Session Duration",
        description="Duration of the voting session in minutes (default=1)",
        ge=1,
    )


class SessionResponseDTO(BaseModel):
    id: Optional[int] = Field(..., title="Session ID")
    topic_id: int = Field(..., title="Topic ID")
    start_time: datetime = Field(..., title="Session Start Time")
    end_time: datetime = Field(..., title="Session End Time")
    duration_minutes: int = Field(..., title="Duration in Minutes")

    @classmethod
    def from_domain(cls, session: DomainSession) -> "SessionResponseDTO":
        return cls(
            id=session.id,
            topic_id=session.topic_id,
            start_time=session.start_time,
            end_time=session.end_time,
            duration_minutes=session.duration_time,
        )

    class Config:
        orm_mode = True
