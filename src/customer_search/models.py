"""Customer domain model."""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Customer:
    """Customer domain model exposing name and email information."""

    name: str
    email: str
    id: Optional[Any] = None

    def __post_init__(self) -> None:
        if not isinstance(self.name, str):
            raise TypeError("Customer name must be a string.")
        if not isinstance(self.email, str):
            raise TypeError("Customer email must be a string.")
