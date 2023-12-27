from typing import Any
from unittest.mock import patch
from cleankedex.application.pokemon.exceptions.pokemon_not_found_exception import (
    PokemonNotFoundException,
)
from fastapi_pagination import add_pagination
import pytest
from fastapi.testclient import TestClient
import httpx
from cleankedex.main import app


# Config
client: TestClient = TestClient(app)
add_pagination(app)

# Urls
base_url_server: str = "http://testserver"
endpoint_get_pokemons: str = "/api/v1/pokemons"
endpoint_get_pokemons_by_id: str = "/api/v1/pokemons/1"

# patch urls
pokemon_read_service_mock: str = (
    "cleankedex.api.pokemon.v1.pokemon_api.PokemonReadService"
)

# Exception messages
generic_not_controlled_exception: str = "Not controlled exception"
generic_not_found_exception: str = "Not found exception"


@pytest.mark.asyncio
async def test_get_pokemons() -> None:
    async with httpx.AsyncClient(app=app, base_url=base_url_server) as client:
        response: Any = await client.get(endpoint_get_pokemons)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_pokemons_not_controlled_exception() -> None:
    with patch(pokemon_read_service_mock) as mock_get_pokemons:
        mock_get_pokemons.side_effect = Exception(generic_not_controlled_exception)

        async with httpx.AsyncClient(app=app, base_url=base_url_server) as client:
            response: Any = await client.get(endpoint_get_pokemons)

    assert response.status_code == 500


@pytest.mark.asyncio
async def test_get_pokemon_by_id() -> None:
    async with httpx.AsyncClient(app=app, base_url=base_url_server) as client:
        response = await client.get(endpoint_get_pokemons_by_id)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_pokemon_by_id_pokemon_not_found_exception() -> None:
    with patch(pokemon_read_service_mock) as mock_get_pokemons:
        mock_get_pokemons.side_effect = PokemonNotFoundException(
            generic_not_found_exception
        )

        async with httpx.AsyncClient(app=app, base_url=base_url_server) as client:
            response: Any = await client.get(endpoint_get_pokemons_by_id)

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_pokemon_by_id_not_controlled_exception() -> None:
    with patch(pokemon_read_service_mock) as mock_get_pokemons:
        mock_get_pokemons.side_effect = Exception(generic_not_controlled_exception)

        async with httpx.AsyncClient(app=app, base_url=base_url_server) as client:
            response: Any = await client.get(endpoint_get_pokemons_by_id)

    assert response.status_code == 500
