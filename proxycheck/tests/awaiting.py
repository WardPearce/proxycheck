import asynctest

from datetime import datetime

from .. import Awaiting
from ..model import IpModel


class TestProxyCheckAwaiting(asynctest.TestCase):
    use_default_loop = True

    def setUp(self):
        self.client = Awaiting()
        self.valid_ip = self.client.ip("98.75.2.4")

    async def tearDown(self):
        await self.client.close()

    async def test_valid_get(self):
        self.assertIsInstance(await self.valid_ip.get(asn=True), IpModel)

    async def test_valid_risk(self):
        self.assertTrue(type(await self.valid_ip.risk()) == int)

    async def test_valid_geological(self):
        latitude, longitude = await self.valid_ip.geological()

        self.assertTrue(type(latitude) == float)
        self.assertTrue(type(longitude) == float)

    async def test_valid_proxy(self):
        self.assertTrue(type(await self.valid_ip.proxy()) == bool)

    async def test_date_field(self):
        self.assertIsInstance(
            await self.valid_ip.get(ver=datetime.now()), IpModel
        )
