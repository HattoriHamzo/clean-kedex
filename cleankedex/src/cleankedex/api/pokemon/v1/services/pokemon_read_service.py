from typing import List
from cleankedex.api.pokemon.v1.request.pokemon_filter_request import (
    PokemonFilterRequest,
)
from cleankedex.api.pokemon.v1.response.pokemon_response import PokemonResponse
from cleankedex.config.application.di_injector import inject
from cleankedex.domain.entities.pokemon.pokemon_entity import Pokemon
from cleankedex.domain.ports.pokemon.pokemon_port import PokemonPort
from cleankedex.config.log.logging import logger
from fastapi_pagination import Page, paginate
from automapper import mapper


class PokemonReadService:
    """Service class for reading Pokemon information."""

    @inject()
    def __init__(self, pokemon_port: PokemonPort) -> None:
        self.pokemon_port = pokemon_port

    async def get_pokemons(self, filter: PokemonFilterRequest) -> Page[PokemonResponse]:
        """Retrieve Pokemon entities based on the provided filter.

        Args:
            filter (PokemonFilterRequest): The filter criteria for querying Pokemon.

        Returns:
            Page[PokemonResponse]: A paginated response containing Pokemon entities.
        """

        logger.debug("get_pokemons started")

        pokemons_entity: List[Pokemon] = await self.pokemon_port.get_pokemons(
            filter=filter
        )

        paginated_pokemons_entity: Page[Pokemon] = paginate(pokemons_entity)

        return paginated_pokemons_entity

    async def get_pokemon_by_id(self, pokemon_id: int) -> PokemonResponse:
        """Get details of a Pokemon by its ID.

        Args:
            pokemon_id (int): The ID of the Pokemon.

        Returns:
            PokemonResponse: Details of the Pokemon.
        """

        logger.debug("get_pokemon_by_id started")

        pokemon_entity: Pokemon = await self.pokemon_port.get_by_id(
            pokemon_id=pokemon_id
        )

        mapped_pokemon: PokemonResponse = mapper.to(PokemonResponse).map(pokemon_entity)

        return mapped_pokemon
