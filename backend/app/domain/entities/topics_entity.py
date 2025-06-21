from typing import Optional


class Topic:
    def __init__(self, title: str, id_: Optional[int] = None):
        """Initializes a Topic entity."""
        self.id = id_ or None
        self.title = title
