from cleankedex.api.pokemon.v1.request.pokemon_filter_request import (
    PokemonFilterRequest,
)
from cleankedex.api.pokemon.v1.response.pokemon_response import PokemonResponse
from cleankedex.api.pokemon.v1.services.pokemon_read_service import PokemonReadService
from cleankedex.application.pokemon.exceptions.pokemon_not_found_exception import (
    PokemonNotFoundException,
)
from cleankedex.config.api.api_message import ApiMessage
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi_pagination import Page
from starlette.requests import Request
from starlette.responses import Response
from cleankedex.config.log.logging import logger


api_router: APIRouter = APIRouter()


@api_router.get(
    "",
    response_model=Page[PokemonResponse],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": ApiMessage,
        },
    },
)
async def get_pokemons_paginated(
    request: Request,
    response: Response,
    filter: PokemonFilterRequest = Depends(),
) -> Page[PokemonResponse]:
    """Retrieve paginated Pokemon entities based on filter criteria.

    This endpoint retrieves a paginated list of Pokemon entities based on the specified filter criteria.

    Args:
        - **pokedex_id** (Optional): ID of the Pokedex (Optional).
        - **name** (Optional): Name of the Pokemon (Optional).
        - **pokemon_type** (Optional): Type of the Pokemon (Optional).
        - **generation** (Optional): Generation of the Pokemon (Optional).
        - **page** (Optional): Page number for pagination (Optional).
        - **size** (Optional): Number of items per page (Optional).

    Returns:
        - `page`: Current page number.
        - `pages`: Total number of pages.
        - `total`: Total number of items.
        - `items`: List of Pokemon entities.

    Raises:
        - `HTTPException` (status code=500): If an internal server error occurs.
    """

    try:
        paginated_pokemon_response: Page[
            PokemonResponse
        ] = await PokemonReadService().get_pokemons(filter=filter)
        return paginated_pokemon_response

    except Exception:
        logger.debug("Not controlled exception")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Something went wrong"},
        )


@api_router.get(
    "/{id:int}",
    response_model=PokemonResponse,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ApiMessage,
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": ApiMessage,
        },
    },
)
async def get_pokemon_by_id(
    request: Request,
    response: Response,
    id: int,
) -> Page[PokemonResponse]:
    """Retrieve details of a Pokemon by its ID.

    This endpoint returns the details of a Pokemon based on the provided ID.

    Args:
        - **id** (int): The ID of the Pokemon to retrieve.

    Raises:
        - `PokemonNotFoundException`: If the Pokemon with the specified ID is not found.
        - `HTTPException`: If an internal server error occurs.
    """

    try:
        pokemon_response: PokemonResponse = (
            await PokemonReadService().get_pokemon_by_id(pokemon_id=id)
        )
        return pokemon_response

    except PokemonNotFoundException:
        logger.debug(f"Pokemon with id {id} not found")
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Something went wrong"},
        )
    except Exception:
        logger.debug("Not controlled exception")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Something went wrong"},
        )
