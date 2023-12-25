from abc import ABCMeta, abstractmethod
from typing import List, Optional
from cleankedex.api.pokemon.v1.request.pokemon_filter_request import (
    PokemonFilterRequest,
)

from cleankedex.domain.entities.pokemon.pokemon_entity import Pokemon


class PokemonPort(metaclass=ABCMeta):
    """Abstract base class representing a port for interacting with Pokemon entities."""

    @abstractmethod
    async def get_pokemons(
        self, filter: PokemonFilterRequest
    ) -> Optional[List[Pokemon]]:
        """Retrieve a list of Pokemon entities based on the provided filter.

        Args:
            filter (PokemonFilterRequest): The filter criteria for querying Pokemon.

        Returns:
            Optional[List[Pokemon]]: A list of Pokemon entities.
        """
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, pokemon_id: int) -> Pokemon:
        """Retrieve a Pokemon entity by its ID.

        Args:
            pokemon_id (int): The ID of the Pokemon.

        Returns:
            Optional[Pokemon]: The Pokemon entity.
        """
        raise NotImplementedError()
