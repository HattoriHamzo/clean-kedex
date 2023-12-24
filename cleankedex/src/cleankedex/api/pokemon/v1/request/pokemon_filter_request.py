from typing import Optional
from pydantic import BaseModel, Field


class PokemonFilterRequest(BaseModel):
    """Request model for filtering Pokemon entities."""

    pokedex_id: Optional[int] = Field(
        description="The Pokedex ID of the Pokemon.", example="1", default=None
    )
    name: Optional[str] = Field(
        description="The name of the Pokemon.", example="Bulbasaur", default=None
    )
    pokemon_type: Optional[str] = Field(
        description="The type of the Pokemon.", example="Grass", default=None
    )
    generation: Optional[int] = Field(
        description="The generation of the Pokemon.", example="1", default=None
    )
