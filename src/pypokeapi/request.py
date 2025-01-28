from __future__ import annotations
import httpx
from typing import Any

class Requester:
    def do_get(url:str)->dict[str, Any]:
        response:httpx.Response = httpx.get(url)
        return response.json()

    @staticmethod
    def Requester_default() -> Requester:
        return Requester()