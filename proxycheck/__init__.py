from .awaiting.ip import AwaitingIp
from .base import Base


class Awaiting(Base):
    def __init__(self, key: str = None) -> None:
        """Interact with Proxycheck.

        Parameters
        ----------
        key : str, optional
        """

        super().__init__(key, True)

    def ip(self, ip: str) -> AwaitingIp:
        return AwaitingIp(ip, self)

    async def close(self) -> None:
        await self.requests.aclose()


class Blocking(Base):
    def __init__(self, key: str = None) -> None:
        """Interact with Proxycheck.

        Parameters
        ----------
        key : str, optional
        """

        super().__init__(key, False)

    def close(self) -> None:
        self.requests.close()
