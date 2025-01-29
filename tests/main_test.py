from pypokeapi.pokemons import Pokemon
import httpx

def test_fetch_ditto():
    response = httpx.get("https://pokeapi.co/api/v2/pokemon/ditto")
    data = response.json()
    
    assert data["name"] == "ditto"
    assert data["id"] == 132
    assert data["height"] == 3
    assert data["name"] == "ditto"
    assert data["weight"] == 40

def test_init_pokemon():
    data = {
        "id": 1,
        "name": "test",
        "height": 3,
        "weight": 40,
        "order": 200,
        "sprites": {
            "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/384.png",
            "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/384.png"
        }
    }
    pokemon = Pokemon(data)

    assert pokemon.id == 1
    assert pokemon.name == "test"
    assert pokemon.height == 3
    assert pokemon.weight == 40
    assert pokemon.order == 200
    assert pokemon.image[0].name == "back_default"
    assert pokemon.image[0].url == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/384.png"

