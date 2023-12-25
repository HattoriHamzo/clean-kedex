from typing import List, Optional
from cleankedex.api.pokemon.v1.request.pokemon_filter_request import (
    PokemonFilterRequest,
)
from cleankedex.application.pokemon.exceptions.pokemon_not_found_exception import (
    PokemonNotFoundException,
)
from cleankedex.config.db.db_connection_manager import DbConnectionManager
from cleankedex.domain.entities.pokemon.pokemon_entity import Pokemon
from cleankedex.domain.models.pokemon.pokemon_model import PokemonModel
from cleankedex.domain.ports.pokemon.pokemon_port import PokemonPort
from automapper import mapper
from cleankedex.utilities.db.query_operations import QueryOperations


class PokemonAdapter(PokemonPort):
    """Adapter class for handling Pokemon-related operations."""

    _model: PokemonModel = PokemonModel

    async def get_pokemons(
        self, filter: PokemonFilterRequest
    ) -> Optional[List[Pokemon]]:
        """Retrieve Pokemon entities based on the provided filter.

        Args:
            filter (PokemonFilterRequest): The filter criteria for querying Pokemon.

        Returns:
            Optional[List[Pokemon]]: A list of Pokemon entities matching the filter.
        """
        with DbConnectionManager() as manager:
            filters: dict = {
                "pokedex_id": filter.pokedex_id,
                "name": filter.name,
                "pokemon_type": filter.pokemon_type,
                "generation": filter.generation,
            }

            queried_pokemon_models: List[
                PokemonModel
            ] = QueryOperations().query_filter_operations(
                manager=manager, model=self._model, filter_by=filters
            )

            mapped_pokemons: List[Pokemon] = [
                mapper.to(Pokemon).map(pokemon) for pokemon in queried_pokemon_models
            ]

            return mapped_pokemons

    async def get_by_id(self, pokemon_id: int) -> Pokemon:
        """Retrieve a Pokemon by its ID.

        Args:
            pokemon_id (int): The ID of the Pokemon.

        Returns:
            Pokemon: The retrieved Pokemon entity.

        Raises:
            PokemonNotFoundException: If the Pokemon with the specified ID is not found.
        """
        with DbConnectionManager() as manager:
            queried_pokemon_model: PokemonModel = (
                manager.session.query(self._model)
                .filter(self._model.id == pokemon_id)
                .first()
            )

            if not queried_pokemon_model:
                raise PokemonNotFoundException(
                    f"Pokemon with id {pokemon_id} not found"
                )

            mapped_pokemon: Pokemon = mapper.to(Pokemon).map(queried_pokemon_model)

            return mapped_pokemon
