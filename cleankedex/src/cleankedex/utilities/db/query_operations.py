import importlib
from types import ModuleType
from typing import Any, List
from cleankedex.config.db.db_connection_manager import DbConnectionManager
from cleankedex.domain.models.pokemon.pokemon_model import PokemonModel


class QueryOperations:
    """
    class for QueryOperations
    """

    # TODO - Future versions may need something more "modular" keep it in mind Pablo, remeber young padwan

    def query_filter_operations(
        self, manager: DbConnectionManager, model: Any, filter_by: dict
    ) -> List[PokemonModel]:
        """Apply dynamic query filters based on the provided filter dictionary.

        Args:
            manager (DbConnectionManager): The database connection manager.
            model (Any): The SQLAlchemy model to query.
            filter_by (dict): A dictionary containing filter criteria.

        Returns:
            List[PokemonModel]: A list of query results after applying filters.
        """

        query: Any = manager.session.query(model)

        for k, v in filter_by.items():
            if v is not None:
                module_name: str = f"cleankedex.domain.filters.pokemon.{k}"
                module: ModuleType = importlib.import_module(module_name)
                method: Any = getattr(module, "filter_by")
                query: Any = method(model, query, v)

        return query
