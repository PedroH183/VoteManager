from typing import Optional
from datetime import datetime, timedelta


class Session:
    def __init__(
        self,
        topic_id: int,
        id_: Optional[int] = None,
        start_time: Optional[datetime] = None,
        duration_minutes: int = 1,
    ):
        self.id       = id_
        self.topic_id = topic_id
        self.start_time = start_time or datetime.now()
        self.end_time   = self.start_time + timedelta(minutes=duration_minutes)

    @property
    def is_open(self) -> bool:
        """Retorna True se a sessão ainda está aberta."""
        return self.start_time <= datetime.now() < self.end_time

    @property
    def has_closed(self) -> bool:
        """Retorna True se a sessão já encerrou."""
        return datetime.now() >= self.end_time

    @property
    def duration_time(self) -> int:
        """Retorna a duração da sessão em minutos."""
        return int((self.end_time - self.start_time).total_seconds() / 60)
    
    @property
    def start_time_str(self) -> str:
        """Retorna a hora de início da sessão como string."""
        return self.start_time.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def end_time_str(self) -> str:
        """Retorna a hora de término da sessão como string."""
        return self.end_time.strftime("%Y-%m-%d %H:%M:%S")
