import unittest

from .. import Blocking
from ..model import IpModel


class TestProxyCheckBlocking(unittest.TestCase):
    use_default_loop = True

    def setUp(self):
        self.client = Blocking()
        self.valid_ip = self.client.ip("98.75.2.4")

    def tearDown(self):
        self.client.close()

    def test_valid_get(self):
        self.assertIsInstance(self.valid_ip.get(asn=True), IpModel)

    def test_valid_risk(self):
        self.assertTrue(type(self.valid_ip.risk()) == int)

    def test_valid_geological(self):
        latitude, longitude = self.valid_ip.geological()

        self.assertTrue(type(latitude) == float)
        self.assertTrue(type(longitude) == float)

    def test_valid_proxy(self):
        self.assertTrue(type(self.valid_ip.proxy()) == bool)
