from typing import Tuple

from ..base import IpBase
from ..model import IpModel
from ..util import format_params


class BlockingIp(IpBase):
    def _get(self, **kwargs) -> IpModel:
        return self._handle_request(
            self._context.requests.get(
                self.url,
                params=format_params(kwargs)
            )
        )

    def proxy(self) -> bool:
        """Used to check if Ip address is proxy.

        Returns
        -------
        bool
            If proxy
        """

        return (self._get(vpn=True)).proxy

    def geological(self) -> Tuple[str, str]:
        """Used to get the longitude & latitude.

        Returns
        -------
        str
            latitude
        str
            longitude
        """

        ip = self._get(asn=True)
        return ip.latitude, ip.longitude

    def risk(self) -> int:
        """Used to get risk value.

        Returns
        -------
        int
        """

        return (self._get(risk=True)).risk

    def get(self, **kwargs) -> IpModel:
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

        return self._get(**kwargs)
