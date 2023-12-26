from typing import List
from unittest.mock import AsyncMock, patch
from cleankedex.api.pokemon.v1.response.pokemon_response import PokemonResponse
from cleankedex.api.pokemon.v1.services.pokemon_read_service import PokemonReadService
from cleankedex.domain.entities.pokemon.pokemon_entity import Pokemon
from fastapi_pagination import Page
import pytest

from tests.utilities.pokemon import (
    create_pokemons_entity,
    create_paginated_pokemon_response,
    create_pokemon_filter_request,
    create_pokemon_entity,
    create_pokemon_response,
)


@pytest.fixture
def mock_get_pokemons() -> AsyncMock:
    pokemons_entity: Pokemon = create_pokemons_entity()

    mock_repo: AsyncMock = AsyncMock()
    mock_repo.get_pokemons = AsyncMock(return_value=pokemons_entity)
    return mock_repo


@pytest.fixture
def mock_get_pokemon_by_id() -> AsyncMock:
    pokemon_entity: Pokemon = create_pokemon_entity(id=1, pokedex_id=1)

    mock_repo: AsyncMock = AsyncMock()
    mock_repo.get_by_id = AsyncMock(return_value=pokemon_entity)
    return mock_repo


# TESTS STARTS HERE #


@pytest.mark.asyncio
async def test_get_pokemons(mock_get_pokemons) -> None:
    with patch(
        "cleankedex.api.pokemon.v1.services.pokemon_read_service.paginate"
    ) as mock_paginate:
        # You have to mock paginate from fastapi_pagination this way because,
        # you will get an error 'add_pagination or params'

        mock_paginate.return_value = create_paginated_pokemon_response()

        pokemon_read_service: PokemonReadService = PokemonReadService(
            pokemon_port=mock_get_pokemons
        )

        expected_result: Page[PokemonResponse] = create_paginated_pokemon_response()

        result: PokemonResponse = await pokemon_read_service.get_pokemons(
            filter=create_pokemon_filter_request(
                pokedex_id=1, name="Bulbasaur", pokemon_type="Grass", generation=1
            )
        )

        assert result == expected_result


@pytest.mark.asyncio
async def test_get_pokemon_by_id(mock_get_pokemon_by_id) -> None:
    pokemon_read_service: PokemonReadService = PokemonReadService(
        pokemon_port=mock_get_pokemon_by_id
    )

    expected_result: PokemonResponse = create_pokemon_response(pokedex_id=1)

    result: PokemonResponse = await pokemon_read_service.get_pokemon_by_id(pokemon_id=1)

    assert result == expected_result
