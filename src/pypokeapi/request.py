from __future__ import annotations
import httpx
from typing import Any

class Requester:
    """
    Classe permettant d'effectuer des requêtes HTTP vers l'API "PokéAPI".

    Utilise le module httpx.
    """
    def do_get(url:str)->dict[str, Any]:
        """
        Effectue une requête GET sur l'URL fournie et retourne le résultat sous forme de dictionnaire.

        Args:
            url (str): L'URL de l'API vers laquelle envoyer la requête.

        Returns:
            (dict[str, Any]): Réponse JSON sous forme de dictionnaire.
        """
        response:httpx.Response = httpx.get(url)
        return response.json()

    @staticmethod
    def Requester_default() -> Requester:
        """
        Méthode de factory retournant une instance de Requester par défaut.

        Returns:
            (Requester): une nouvelle instance de Requester.
        """
        return Requester()