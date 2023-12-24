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
    """Endpoint to retrieve paginated Pokemon entities based on the provided filter.

    Args:
        request (Request): The FastAPI request object.
        response (Response): The FastAPI response object.
        filter (PokemonFilterRequest, optional): The filter criteria for querying Pokemon.
            Defaults to Depends().

    Returns:
        Page[PokemonResponse]: A paginated response containing Pokemon entities.
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
