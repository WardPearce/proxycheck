from .awaiting.ip import AwaitingIp
from .blocking.ip import BlockingIp
from .base import Base


__version__ = "0.0.1"
__url__ = "https://proxycheck.readthedocs.io/en/latest/"
__description__ = "Wrapper for Proxycheck's API."
__author__ = "WardPearce"
__author_email__ = "wardpearce@protonmail.com"
__license__ = "GPL-3.0 License"


class Awaiting(Base):
    def __init__(self, key: str = None) -> None:
        """Interact with Proxycheck.

        Parameters
        ----------
        key : str, optional
        """

        super().__init__(key, True)

    def ip(self, ip: str) -> AwaitingIp:
        """Used to pull details on a IP.

        Parameters
        ----------
        ip : str

        Returns
        -------
        AwaitingIp
        """

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

    def ip(self, ip: str) -> BlockingIp:
        """Used to pull details on a IP.

        Parameters
        ----------
        ip : str

        Returns
        -------
        BlockingIp
        """
        return BlockingIp(ip, self)

    def close(self) -> None:
        self.requests.close()
