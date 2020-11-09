import logging

from httpx import AsyncClient, Client, Response

from .model import IpModel
from .exceptions import QueryFailed, QueryDenied


class Base:
    API_URL = "https://proxycheck.io/v2/"

    def __init__(self, key: str, awaiting: bool) -> None:
        client = AsyncClient if awaiting else Client
        self.requests = client(params={"key": key} if key else None)


class IpBase:
    def __init__(self, ip: str, context: object) -> None:
        self.ip = ip
        self.url = context.API_URL + ip
        self._context = context

    def _handle_request(self, resp: Response) -> IpModel:
        resp.raise_for_status()

        resp_json = resp.json()
        if resp_json["status"] in ("ok", "warning"):
            if resp_json["status"] == "warning":
                logging.warning(resp_json["message"])

            return IpModel(resp_json[self.ip])
        elif resp_json["status"] == "error":
            raise QueryFailed(resp_json["message"])
        else:
            raise QueryDenied(resp_json["message"])
