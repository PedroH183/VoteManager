from typing import Optional


class Vote:
    def __init__(self, option: str, session_id: int, id_: Optional[int] = None):
        """Initializes a Vote entity."""

        self.id = id_
        self.option = option
        # self.user_id = user_id
        self.session_id = session_id
