from pypokeapi.pokemons import Pokemon
from pypokeapi.request import Requester
import httpx


def test_fetch_ditto():
    """
    L’objectif de ce test est de tester que la lib httpx fait bien ce qu’on veux.

    - Effectue un appel de l'API pour fetch ditto.
    - Vérifie que les valeurs du dictionnaire de résultat sont bien conformes.
    """
    response = httpx.get("https://pokeapi.co/api/v2/pokemon/ditto")
    data = response.json()

    assert data["id"] == 132
    assert data["name"] == "ditto"
    assert data["height"] == 3
    assert data["weight"] == 40
    assert data["order"] == 214


def test_init_pokemon():
    data = {
        "id": 1,
        "name": "test",
        "height": 3,
        "weight": 40,
        "order": 200,
        "sprites": {
            "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/384.png",
            "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/384.png",
        },
    }
    pokemon = Pokemon(data)

    assert pokemon.id == 1
    assert pokemon.name == "test"
    assert pokemon.height == 3
    assert pokemon.weight == 40
    assert pokemon.order == 200
    assert pokemon.image[0].name == "front_default"
    assert (
        pokemon.image[0].url
        == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/384.png"
    )


def test_from_name():
    pokemon = Pokemon.from_name("ditto")

    assert pokemon.id == 132
    assert pokemon.name == "ditto"
    assert pokemon.height == 3
    assert pokemon.weight == 40
    assert pokemon.order == 214
    assert pokemon.image[0].name == "front_default"
    assert (
        pokemon.image[0].url
        == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png"
    )


def test_from_id():
    pokemon = Pokemon.from_id(132)

    assert pokemon.id == 132
    assert pokemon.name == "ditto"
    assert pokemon.height == 3
    assert pokemon.weight == 40
    assert pokemon.order == 214
    assert pokemon.image[0].name == "front_default"
    assert (
        pokemon.image[0].url
        == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png"
    )


def test_get_moves():
    pokemon = Pokemon.from_name("ditto")

    assert pokemon.get("moves")[0].get("move").get("name") == "transform"
    assert (
        pokemon.get("moves")[0].get("move").get("url")
        == "https://pokeapi.co/api/v2/move/144/"
    )


def test_fetch_image():
    pokemon = Pokemon.from_name("pikachu")
    images = pokemon.image

    assert images[0].name == "front_default"
    assert images[1].name == "back_default"
    assert images[2].name == "front_female"
    assert images[3].name == "back_female"
    assert images[4].name == "front_shiny"
    assert images[5].name == "back_shiny"
    assert images[6].name == "front_shiny_female"
    assert images[7].name == "back_shiny_female"


def test_random_requester():
    RandomRequester = Requester()
