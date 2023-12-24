from fastapi import APIRouter

from cleankedex.api.pokemon.v1 import pokemon_api

api_router: APIRouter = APIRouter()
api_router.include_router(
    pokemon_api.api_router, prefix="/api/v1/pokemons", tags=["Pokemons"]
)
