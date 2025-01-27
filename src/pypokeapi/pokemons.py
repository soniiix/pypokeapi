from __future__ import annotations
import httpx
from request import Requester


class Image:
    def __init__(self, name:str, url:str):
        self.name = name
        self.url = url


class Pokemon :
    def __init__(self, data:dict[str, any], requester:Requester = None):
        self.id:int = data['id']
        self.name:str = data['name']
        self.height:float = data['height']
        self.image:Image = data['image']
        self.order:int = data['order']
        self.weight:float = data['weight']
        self._requester = requester
        self._data = data

    def get(attr:str)->dict[str, any]:
        pass
    
    @staticmethod
    def from_id(id:int, requester:Requester = None) -> Pokemon:
        url:str = "https://pokeapi.co/api/v2/pokemon/" + id
        r:httpx.Response = Requester.do_get(url)
        pokemon:Pokemon = Pokemon(r.text)
        return pokemon

    @staticmethod
    def from_name(name:str, requester:Requester = None) -> Pokemon:
        url:str = "https://pokeapi.co/api/v2/pokemon/" + name
        r:httpx.Response = Requester.do_get(url)
        pokemon:Pokemon = Pokemon(r.text)
        return pokemon

