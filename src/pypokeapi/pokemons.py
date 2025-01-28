from __future__ import annotations
from pypokeapi.request import Requester
from typing import Any

class Image:
    name:str
    url:str

    def __init__(self, name:str, url:str):
        self.name = name
        self.url = url

class Pokemon :
    id:int
    name:str
    height:float
    image:list[Image]
    order:int
    weight:float
    _requester:dict
    _data:dict[str, Any]

    def __init__(self, data:dict[str, Any], requester:Requester = None):
        self.id = data['id']
        self.name = data['name']
        self.height = data['height']
        self.image = data['sprites']

        for name, url in data['sprites'].items():
            if url is not None:
                self.image.append(Image(name, url))

        self.order = data['order']
        self.weight = data['weight']
        self._requester = requester
        self._data = data

    def get(self, attr:str) -> dict[str, Any]:
        return self._data[attr]
    
    @staticmethod
    def from_id(id:int, requester:Requester = None) -> Pokemon:
        if requester is None:
            requester = Requester.Requester_default()
        url:str = f"https://pokeapi.co/api/v2/pokemon/{id}"
        data:dict[str] = Requester.do_get(url)
        pokemon:Pokemon = Pokemon(data, requester)
        return pokemon

    @staticmethod
    def from_name(name:str, requester:Requester = None) -> Pokemon:
        if requester is None:
            requester = Requester.Requester_default()
        url:str = f"https://pokeapi.co/api/v2/pokemon/{name}"
        data:dict[str] = Requester.do_get(url)
        pokemon:Pokemon = Pokemon(data, requester)
        return pokemon

