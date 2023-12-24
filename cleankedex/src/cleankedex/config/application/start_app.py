from fastapi import FastAPI
from fastapi_pagination import add_pagination
from pythondi import Provider, configure

from cleankedex.routes import include_routers

from cleankedex.config.log.logging import logger
from cleankedex.config.dependency_injection.di import include_di


def start_application(app: FastAPI):
    """Start the application launching all required modules

    Returns:
        _type_: _description_
    """

    # Dependency injection (general)
    provider: Provider = Provider()
    include_di(provider=provider)
    configure(provider=provider)
    add_pagination(app)
    include_routers(app)

    logger.info("Ready to start ...")
    return app
