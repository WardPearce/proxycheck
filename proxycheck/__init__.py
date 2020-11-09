from typing import Any
from httpx import AsyncClient, Client, Response

from .awaiting.ip import AwaitingIP


class Base:
    API_URL = "https://proxycheck.io/v2/"

    def _handle_request(self, resp: Response, ip: str) -> Any:
        resp.raise_for_status()
        resp_json = resp.json()

        if resp_json["status"] == "ok":
            return resp_json[ip]


class Awaiting(Base):
    def __init__(self, key: str = None) -> None:
        """Interact with Proxycheck.

        Parameters
        ----------
        key : str, optional
        """

        super().__init__()
        self.requests = AsyncClient(params={"key": key} if key else None)

    async def _get(self, ip: str, **kwargs) -> dict:
        return self._handle_request(
            await self.requests.get(self.API_URL + ip, params=kwargs),
            ip
        )

    def ip(self, ip: str) -> AwaitingIP:
        pass

    async def close(self) -> None:
        await self.requests.aclose()


class Blocking(Base):
    def __init__(self, key: str = None) -> None:
        """Interact with Proxycheck.

        Parameters
        ----------
        key : str, optional
        """

        super().__init__()
        self.requests = Client(params={"key": key} if key else None)

    def _get(self, ip: str, **kwargs) -> dict:
        return self._handle_request(
            self.requests.get(self.API_URL + ip, params=kwargs),
            ip
        )

    def close(self) -> None:
        self.requests.close()
