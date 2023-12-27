from typing import List
from cleankedex.api.pokemon.v1.request.pokemon_filter_request import (
    PokemonFilterRequest,
)
from cleankedex.api.pokemon.v1.response.pokemon_response import PokemonResponse
from cleankedex.domain.entities.pokemon.pokemon_entity import Pokemon
from cleankedex.domain.models.pokemon.pokemon_model import PokemonModel
from fastapi_pagination import Page

# Singles


def create_pokemon_model(id: int, pokedex_id: int) -> PokemonModel:
    """ """
    pokemon_model: PokemonModel = PokemonModel(
        id=id,
        pokedex_id=pokedex_id,
        name="Bulbasaur",
        type_1="Grass",
        type_2="Poison",
        total=318,
        hp=45,
        attack=49,
        defense=49,
        sp_attack=65,
        sp_defense=65,
        speed=45,
        generation=1,
    )
    return pokemon_model


def create_pokemon_entity(id: int, pokedex_id: int) -> Pokemon:
    """ """
    pokemon_entity: Pokemon = Pokemon(
        id=id,
        pokedex_id=pokedex_id,
        name="Bulbasaur",
        type_1="Grass",
        type_2="Poison",
        total=318,
        hp=45,
        attack=49,
        defense=49,
        sp_attack=65,
        sp_defense=65,
        speed=45,
        generation=1,
    )
    return pokemon_entity


def create_pokemon_response(pokedex_id: int) -> PokemonResponse:
    """ """
    pokemon_response: PokemonResponse = PokemonResponse(
        pokedex_id=pokedex_id,
        name="Bulbasaur",
        type_1="Grass",
        type_2="Poison",
        total=318,
        hp=45,
        attack=49,
        defense=49,
        sp_attack=65,
        sp_defense=65,
        speed=45,
        generation=1,
    )
    return pokemon_response


# List


def create_pokemons_model() -> List[PokemonModel]:
    """ """
    pokemons_model: List[PokemonModel] = [
        PokemonModel(
            id=1,
            pokedex_id=1,
            name="Bulbasaur",
            type_1="Grass",
            type_2="Poison",
            total=318,
            hp=45,
            attack=49,
            defense=49,
            sp_attack=65,
            sp_defense=65,
            speed=45,
            generation=1,
        ),
        PokemonModel(
            id=2,
            pokedex_id=2,
            name="Ivysaur",
            type_1="Grass",
            type_2="Poison",
            total=405,
            hp=60,
            attack=62,
            defense=63,
            sp_attack=80,
            sp_defense=80,
            speed=60,
            generation=1,
        ),
        PokemonModel(
            id=3,
            pokedex_id=3,
            name="Venusaur",
            type_1="Grass",
            type_2="Poison",
            total=525,
            hp=80,
            attack=82,
            defense=83,
            sp_attack=100,
            sp_defense=100,
            speed=80,
            generation=1,
        ),
    ]
    return pokemons_model


def create_pokemons_entity() -> List[Pokemon]:
    """ """
    pokemons_entity: List[Pokemon] = [
        Pokemon(
            id=1,
            pokedex_id=1,
            name="Bulbasaur",
            type_1="Grass",
            type_2="Poison",
            total=318,
            hp=45,
            attack=49,
            defense=49,
            sp_attack=65,
            sp_defense=65,
            speed=45,
            generation=1,
        ),
        Pokemon(
            id=2,
            pokedex_id=2,
            name="Ivysaur",
            type_1="Grass",
            type_2="Poison",
            total=405,
            hp=60,
            attack=62,
            defense=63,
            sp_attack=80,
            sp_defense=80,
            speed=60,
            generation=1,
        ),
        Pokemon(
            id=3,
            pokedex_id=3,
            name="Venusaur",
            type_1="Grass",
            type_2="Poison",
            total=525,
            hp=80,
            attack=82,
            defense=83,
            sp_attack=100,
            sp_defense=100,
            speed=80,
            generation=1,
        ),
    ]
    return pokemons_entity


# paginated PokemonResponse


def create_paginated_pokemon_response() -> Page[PokemonResponse]:
    paginated_pokemon_response: Page[PokemonResponse] = Page[PokemonResponse](
        items=[
            PokemonResponse(
                pokedex_id=1,
                name="Bulbasaur",
                type_1="Grass",
                type_2="Poison",
                total=318,
                hp=45,
                attack=49,
                defense=49,
                sp_attack=65,
                sp_defense=65,
                speed=45,
                generation=1,
            ),
            PokemonResponse(
                pokedex_id=2,
                name="Ivysaur",
                type_1="Grass",
                type_2="Poison",
                total=405,
                hp=60,
                attack=62,
                defense=63,
                sp_attack=80,
                sp_defense=80,
                speed=60,
                generation=1,
            ),
            PokemonResponse(
                pokedex_id=3,
                name="Venusaur",
                type_1="Grass",
                type_2="Poison",
                total=525,
                hp=80,
                attack=82,
                defense=83,
                sp_attack=100,
                sp_defense=100,
                speed=80,
                generation=1,
            ),
        ],
        total=3,
        page=1,
        size=50,
        pages=1,
    )

    return paginated_pokemon_response


# Filter


def create_pokemon_filter_request(
    pokedex_id: int, name: str, pokemon_type: str, generation: int
) -> PokemonFilterRequest:
    """ """

    pokemon_filter_request: PokemonFilterRequest = PokemonFilterRequest(
        pokedex_id=pokedex_id,
        name=name,
        pokemon_type=pokemon_type,
        generation=generation,
    )

    return pokemon_filter_request
