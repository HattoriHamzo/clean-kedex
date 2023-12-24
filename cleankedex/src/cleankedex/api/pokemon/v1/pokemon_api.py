from cleankedex.api.pokemon.v1.request.pokemon_filter_request import (
    PokemonFilterRequest,
)
from cleankedex.api.pokemon.v1.response.pokemon_response import PokemonResponse
from cleankedex.api.pokemon.v1.services.pokemon_read_service import PokemonReadService
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
async def get_pokemons(
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
        pokemons_response: Page[
            PokemonResponse
        ] = await PokemonReadService().get_pokemons(filter=filter)
        return pokemons_response

    except Exception:
        logger.exception("Not controlled exception")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Something went wrong"},
        )
