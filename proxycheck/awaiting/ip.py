from typing import Tuple, Union, TYPE_CHECKING

from ..base import IpBase
from ..model import IpModel
from ..util import format_params

if TYPE_CHECKING:
    from .. import Awaiting


class AwaitingIp(IpBase):
    _context: "Awaiting"

    async def _get(self, **kwargs) -> IpModel:
        return self._handle_request(
            await self._context.requests.get(
                self.url,
                params=format_params(kwargs)
            )
        )

    async def proxy(self) -> Union[bool, None]:
        """Used to check if Ip address is proxy.

        Returns
        -------
        bool
            If proxy
        """

        return (await self._get(vpn=True)).proxy

    async def geological(self
                         ) -> Tuple[Union[float, None], Union[float, None]]:
        """Used to get the longitude & latitude.

        Returns
        -------
        str
            latitude
        str
            longitude
        """

        ip = await self._get(asn=True)
        return ip.latitude, ip.longitude

    async def risk(self) -> Union[int, None]:
        """Used to get risk value.

        Returns
        -------
        int
        """

        return (await self._get(risk=True)).risk

    async def get(self, **kwargs) -> IpModel:
        """Used to get details on a IP.

        Parameters
        ----------
        vpn : bool, optional
            by default True
        asn : bool, optional
            by default False
        node : bool, optional
            by default False
        time : bool, optional
            by default False
        inf : bool, optional
            by default False
        risk : bool, optional
            by default False
        port : bool, optional
            by default False
        seen : bool, optional
            by default False
        days : int, optional
            by default None
        tag : str, optional
            by default None
        ver : datetime, optional
            by default None

        Returns
        -------
        IpModel

        Raises
        ------
        QueryFailed
        QueryDenied
        HTTPError
            https://www.python-httpx.org/exceptions/#the-exception-hierarchy
        """

        return await self._get(**kwargs)
