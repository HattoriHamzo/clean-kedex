from cleankedex.config.db.base_model import Base
from sqlalchemy import (
    Column,
    String,
    Integer,
)


class PokemonModel(Base):
    """
    Represents a Pokemon model for database storage.

    Attributes:
    - __tablename__ (str): The name of the table in the database where Pokemon data is stored.
    """

    __tablename__ = "pokemon"

    id: int = Column(Integer, primary_key=True, index=True, nullable=False)
    pokedex_id: int = Column(Integer, nullable=False)
    name: str = Column(String(50), nullable=False)
    type_1: str = Column(String(50), nullable=True)
    type_2: str = Column(String(50), nullable=True)
    total: int = Column(Integer, nullable=True)
    hp: int = Column(Integer, nullable=True)
    attack: int = Column(Integer, nullable=True)
    defense: int = Column(Integer, nullable=True)
    sp_attack: int = Column(Integer, nullable=True)
    sp_defense: int = Column(Integer, nullable=True)
    speed: int = Column(Integer, nullable=True)
    generation: int = Column(Integer, nullable=False)
