from typing import Any
from sqlalchemy.orm import Query


def filter_by(model: Any, query: Query, value: Any) -> Query:
    """Filter query based on a case-insensitive partial match on the 'name' attribute.

    Args:
        model (Any): The SQLAlchemy model.
        query (Query): The current SQLAlchemy query.
        value (Any): The value to filter on (partial match on 'name').

    Returns:
        Query: The filtered SQLAlchemy query.
    """
    query: Any = query.filter(model.name.ilike(f"%{value}%"))

    return query
