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
    """
    Classe décrivant un pokémon.

    Attributes:
        id (int): Identifiant unique du Pokémon.
        name (str): Nom du Pokémon.
        height (float): Taille du Pokémon.
        image (list[Image]): Liste des images du Pokémon.
        order (int): ?
        weight (float): Poids du Pokémon.
        _requester (dict): Objet permettant de faire des requêtes.
        _data (dict[str, Any]): Tableau de données du Pokémon issues de l'API.
    """

    id:int
    name:str
    height:float
    image:list[Image]
    order:int
    weight:float
    _requester:dict
    _data:dict[str, Any]

    def __init__(self, data:dict[str, Any], requester:Requester = None):
        """
        Constructeur de la classe qui initialise un Pokémon avec les données fournies.

        Args:
            data (dict[str, Any]): Tableau de données contenant toutes les informations d'un Pokémon.
            requester (Requester, optional): Objet permettant de faire des requêtes à l'API.
        """
        self.id = data['id']
        self.name = data['name']
        self.height = data['height']

        self.image = []
        image_order = ["front_default", "back_default", "front_female", "back_female", "front_shiny",
        "back_shiny", "front_shiny_female", "back_shiny_female"]
        for name in image_order:
            url = data['sprites'].get(name)
            if url is not None:
                self.image.append(Image(name, url))

        self.order = data['order']
        self.weight = data['weight']
        self._requester = requester
        self._data = data

    def get(self, attr:str) -> dict[str, Any]:
        """
        Récupère une valeur spécifique parmi les données d'un Pokémon.

        Args:
            attr (str): Clé de l'attribut à récupérer.

        Returns:
            (dict[str, Any]): Valeur correspondante de l'attribut demandé.
        """
        return self._data[attr]
    
    @staticmethod
    def from_id(id:int, requester:Requester = None) -> Pokemon:
        """
        Récupère un Pokémon par son id.

        Args:
            id (int): l'id du Pokémon.
            requester (Requester, optional): Objet permettant de faire des requêtes à l'API.

        Returns:
            (Pokemon): une instance de Pokémon correspondant.
        """
        if requester is None:
            requester = Requester.Requester_default()
        url:str = f"https://pokeapi.co/api/v2/pokemon/{id}"
        data:dict[str] = Requester.do_get(url)
        pokemon:Pokemon = Pokemon(data, requester)
        return pokemon

    @staticmethod
    def from_name(name:str, requester:Requester = None) -> Pokemon:
        """
        Récupère un Pokémon par son nom.

        Args:
            name (str): le nom du Pokémon.
            requester (Requester, optional): Objet permettant de faire des requêtes à l'API.

        Returns:
            (Pokemon): une instance de Pokémon correspondant.
        """
        if requester is None:
            requester = Requester.Requester_default()
        url:str = f"https://pokeapi.co/api/v2/pokemon/{name}"
        data:dict[str] = Requester.do_get(url)
        pokemon:Pokemon = Pokemon(data, requester)
        return pokemon