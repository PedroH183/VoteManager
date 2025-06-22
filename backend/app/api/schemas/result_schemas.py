from pydantic import BaseModel, Field

class VoteResultDTO(BaseModel):
    topic_id: int = Field(..., title="Topic ID")
    session_id: int = Field(..., title="Session ID")
    total_sim: int = Field(..., title="Total 'Sim' votes")
    total_nao: int = Field(..., title="Total 'Não' votes")

    class Config:
        from_attributes = True
