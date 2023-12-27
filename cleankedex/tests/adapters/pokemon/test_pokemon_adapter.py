from typing import List
from unittest.mock import Mock, patch
from cleankedex.adapters.pokemon.pokemon_adapter import PokemonAdapter
from cleankedex.api.pokemon.v1.request.pokemon_filter_request import (
    PokemonFilterRequest,
)
from cleankedex.application.pokemon.exceptions.pokemon_not_found_exception import (
    PokemonNotFoundException,
)
from cleankedex.domain.entities.pokemon.pokemon_entity import Pokemon
from cleankedex.domain.models.pokemon.pokemon_model import PokemonModel
import pytest

from tests.utilities.pokemon import (
    create_pokemons_model,
    create_pokemon_model,
    create_pokemons_entity,
    create_pokemon_entity,
)


# patch urls
db_connection_manager: str = (
    "cleankedex.adapters.pokemon.pokemon_adapter.DbConnectionManager"
)

# FIXTURES STARTS HERE #


@pytest.fixture
def mock_get_pokemons() -> Mock:
    pokemons_model: List[PokemonModel] = create_pokemons_model()

    mock_database: Mock = Mock()
    mock_database.query = Mock(return_value=pokemons_model)
    return mock_database


@pytest.fixture
def mock_get_pokemons_filter() -> Mock:
    pokemons_model: List[PokemonModel] = [create_pokemon_model(id=1, pokedex_id=1)]

    mock_database: Mock = Mock()
    mock_database.query.return_value.filter = Mock(return_value=pokemons_model)
    return mock_database


@pytest.fixture
def mock_get_pokemon_by_id() -> Mock:
    pokemon_model: PokemonModel = create_pokemon_model(id=1, pokedex_id=1)

    mock_database: Mock = Mock()
    mock_database.query.return_value.filter.return_value.first = Mock(
        return_value=pokemon_model
    )
    return mock_database


@pytest.fixture
def mock_get_pokemon_by_id_not_found() -> Mock:
    mock_database: Mock = Mock()
    mock_database.query.return_value.filter.return_value.first = Mock(return_value=None)
    return mock_database


# TESTS STARTS HERE #


@pytest.mark.asyncio
async def test_get_pokemons_without_filters(mock_get_pokemons):
    with patch(db_connection_manager) as connection:
        connection.return_value.__enter__.return_value.session = mock_get_pokemons

        pokemon_filter_request: PokemonFilterRequest = PokemonFilterRequest()

        pokemon_adapter: PokemonAdapter = PokemonAdapter()

        expected_result: List[Pokemon] = create_pokemons_entity()

        result: List[Pokemon] = await pokemon_adapter.get_pokemons(
            filter=pokemon_filter_request
        )

    assert result == expected_result


@pytest.mark.asyncio
async def test_get_pokemons_with_pokedex_id_filter(mock_get_pokemons_filter):
    with patch(db_connection_manager) as connection:
        connection.return_value.__enter__.return_value.session = (
            mock_get_pokemons_filter
        )

        pokemon_filter_request: PokemonFilterRequest = PokemonFilterRequest(
            pokedex_id=1
        )

        pokemon_adapter: PokemonAdapter = PokemonAdapter()

        expected_result: List[Pokemon] = [create_pokemon_entity(id=1, pokedex_id=1)]

        result: List[Pokemon] = await pokemon_adapter.get_pokemons(
            filter=pokemon_filter_request
        )

    assert result == expected_result


@pytest.mark.asyncio
async def test_get_pokemons_with_name_filter(mock_get_pokemons_filter):
    with patch(db_connection_manager) as connection:
        connection.return_value.__enter__.return_value.session = (
            mock_get_pokemons_filter
        )

        pokemon_filter_request: PokemonFilterRequest = PokemonFilterRequest(
            name="Bulbasaur"
        )

        pokemon_adapter: PokemonAdapter = PokemonAdapter()

        expected_result: List[Pokemon] = [create_pokemon_entity(id=1, pokedex_id=1)]

        result: List[Pokemon] = await pokemon_adapter.get_pokemons(
            filter=pokemon_filter_request
        )

    assert result == expected_result


@pytest.mark.asyncio
async def test_get_pokemons_with_pokemon_type_filter(mock_get_pokemons_filter):
    with patch(db_connection_manager) as connection:
        connection.return_value.__enter__.return_value.session = (
            mock_get_pokemons_filter
        )

        pokemon_filter_request: PokemonFilterRequest = PokemonFilterRequest(
            pokemon_type="Grass"
        )

        pokemon_adapter: PokemonAdapter = PokemonAdapter()

        expected_result: List[Pokemon] = [create_pokemon_entity(id=1, pokedex_id=1)]

        result: List[Pokemon] = await pokemon_adapter.get_pokemons(
            filter=pokemon_filter_request
        )

    assert result == expected_result


@pytest.mark.asyncio
async def test_get_pokemons_with_generation_filter(mock_get_pokemons_filter):
    with patch(db_connection_manager) as connection:
        connection.return_value.__enter__.return_value.session = (
            mock_get_pokemons_filter
        )

        pokemon_filter_request: PokemonFilterRequest = PokemonFilterRequest(
            generation=1
        )

        pokemon_adapter: PokemonAdapter = PokemonAdapter()

        expected_result: List[Pokemon] = [create_pokemon_entity(id=1, pokedex_id=1)]

        result: List[Pokemon] = await pokemon_adapter.get_pokemons(
            filter=pokemon_filter_request
        )

    assert result == expected_result


@pytest.mark.asyncio
async def test_get_pokemon_by_id(mock_get_pokemon_by_id):
    with patch(db_connection_manager) as connection:
        connection.return_value.__enter__.return_value.session = mock_get_pokemon_by_id

        pokemon_adapter: PokemonAdapter = PokemonAdapter()

        expected_result: Pokemon = create_pokemon_entity(id=1, pokedex_id=1)

        result: Pokemon = await pokemon_adapter.get_by_id(pokemon_id=1)

    assert result == expected_result


@pytest.mark.asyncio
async def test_get_pokemon_by_id_not_found_exception(mock_get_pokemon_by_id_not_found):
    with patch(db_connection_manager) as connection:
        connection.return_value.__enter__.return_value.session = (
            mock_get_pokemon_by_id_not_found
        )

        pokemon_adapter: PokemonAdapter = PokemonAdapter()

        with pytest.raises(PokemonNotFoundException):
            await pokemon_adapter.get_by_id(pokemon_id=0)
