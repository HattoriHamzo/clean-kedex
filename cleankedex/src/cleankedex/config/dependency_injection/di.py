from cleankedex.adapters.pokemon.pokemon_adapter import PokemonAdapter
from cleankedex.domain.ports.pokemon.pokemon_port import PokemonPort
from pythondi import Provider
from cleankedex.config.log.logging import logger


def include_di(provider: Provider):
    """Initialize dependency injection for repositories

    Args:
        app (_type_): _description_
    """
    logger.debug("Initializing dependency injection")

    # Include your modules
    provider.bind(PokemonPort, PokemonAdapter)
