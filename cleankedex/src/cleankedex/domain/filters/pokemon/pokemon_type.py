from typing import Any
from sqlalchemy import or_
from sqlalchemy.orm import Query


def filter_by(model: Any, query: Query, value: Any) -> Query:
    """Filter query based on a case-insensitive partial match on 'type_1' or 'type_2' attributes.

    Args:
        model (Any): The SQLAlchemy model.
        query (Query): The current SQLAlchemy query.
        value (Any): The value to filter on (partial match on 'type_1' or 'type_2').

    Returns:
        Query: The filtered SQLAlchemy query.
    """
    query: Any = query.filter(
        or_(model.type_1.ilike(f"%{value}%"), model.type_2.ilike(f"%{value}%"))
    )

    return query
