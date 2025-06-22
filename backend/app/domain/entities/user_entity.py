from typing import Optional


class User:
    def __init__(
            self, cpf: str, name: str, password: str, id_: Optional[int] = None
        ):
        """Initializes a User entity."""

        self.id = id_
        self.cpf = cpf
        self.name = name
        self.password = password
