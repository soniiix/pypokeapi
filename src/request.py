from __future__ import annotations
import httpx

class Requester:
    def do_get(url:str)->httpx.Response:
        r:httpx.Response = httpx.get(url)
        return r

    def Requester_default() -> Requester:
        return Requester()