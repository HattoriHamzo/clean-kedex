"""Module to include the API routers for the application
"""
from fastapi import FastAPI
from cleankedex.config.log.logging import logger
from cleankedex.api.pokemon.v1.pokemon_router import api_router as pokemon_v1_router


def include_routers(app: FastAPI) -> None:
    """Include routers in the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application to include routers in.

    Returns:
        None
    """
    logger.debug("Including routers")

    app.include_router(pokemon_v1_router)
