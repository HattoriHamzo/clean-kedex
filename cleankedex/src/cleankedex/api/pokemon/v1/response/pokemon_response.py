from typing import Optional

from pydantic import BaseModel, Field


class PokemonResponse(BaseModel):
    """Response model representing Pokemon entity information."""

    pokedex_id: int = Field(
        description="The Pokedex ID of the Pokemon.",
        example="1",
    )
    name: str = Field(
        description="The name of the Pokemon.",
        example="Bulbasaur",
    )
    type_1: Optional[str] = Field(
        description="The primary type of the Pokemon.",
        example="Grass",
    )
    type_2: Optional[str] = Field(
        description="The secondary type of the Pokemon.",
        example="Poison",
    )
    total: Optional[int] = Field(
        description="The total base stats of the Pokemon.",
        example="318",
    )
    hp: Optional[int] = Field(
        description="The hit points stat of the Pokemon.",
        example="45",
    )
    attack: Optional[int] = Field(
        description="The attack stat of the Pokemon.",
        example="49",
    )
    defense: Optional[int] = Field(
        description="The defense stat of the Pokemon.",
        example="49",
    )
    sp_attack: Optional[int] = Field(
        description="The special attack stat of the Pokemon.",
        example="65",
    )
    sp_defense: Optional[int] = Field(
        description="The special defense stat of the Pokemon.",
        example="65",
    )
    speed: Optional[int] = Field(
        description="The speed stat of the Pokemon.",
        example="45",
    )
    generation: int = Field(
        description="The generation in which the Pokemon was introduced.",
        example="1",
    )
