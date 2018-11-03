import unittest

from src.telnet_client import TelnetClient


class TestConnect(unittest.TestCase):

    def test_connect(self):
        print(11)
        host = "192.168.0.4"
        user = "test1233"
        password = "xxxxxx."
        telnet_client = TelnetClient()
        telnet_client.connect(host, user, password)

    def test_connect_failed(self):
        host = "192.168.0.41"
        user = "test12"
        password = "xxxxxx."
        telnet_client = TelnetClient()
        telnet_client.connect(host, user, password)

    def test_disconnect(self):
        host = "192.168.0.4"
        user = "test1233"
        password = "xxxxxx."
        telnet_client = TelnetClient()
        telnet_client.connect(host, user, password)
        telnet_client.disconnect()
