from typing import Any
from sqlalchemy.orm import Query


def filter_by(model: Any, query: Query, value: Any) -> Query:
    """Filter query based on the specified generation value.

    Args:
        model (Any): The SQLAlchemy model.
        query (Query): The current SQLAlchemy query.
        value (Any): The value to filter on (generation).

    Returns:
        Query: The filtered SQLAlchemy query.
    """
    query: Any = query.filter(model.generation == value)

    return query
