from dataclasses import dataclass, field
from typing import Optional


@dataclass(slots=True)
class Pokemon:
    """
    Represents a Pokemon data model.
    """

    id: int = field(default=None)
    pokedex_id: int = field(default=None)
    name: str = field(default=None)
    type_1: Optional[str] = field(default=None)
    type_2: Optional[str] = field(default=None)
    total: Optional[int] = field(default=None)
    hp: Optional[int] = field(default=None)
    attack: Optional[int] = field(default=None)
    defense: Optional[int] = field(default=None)
    sp_attack: Optional[int] = field(default=None)
    sp_defense: Optional[int] = field(default=None)
    speed: Optional[int] = field(default=None)
    generation: int = field(default=None)
