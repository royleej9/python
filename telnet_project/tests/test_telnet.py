import logging
import sys
import unittest

# from src.telnet_client import TelnetClient
# from .context import src
from src.telnet_client import TelnetClient

# from .context import src
LOGGER = logging.getLogger()
LOGGER.level = logging.DEBUG
STREAM_HANDLER = logging.StreamHandler(sys.stdout)
LOGGER.addHandler(STREAM_HANDLER)


class TestTelnet(unittest.TestCase):

    def test_get_host(self):
        host = "192.168.0.4"
        user = "test1233"
        password = "xxxxxx."

        telnet_client = TelnetClient()
        telnet_client.connect(host, user, password)

        # telnet_client.send("ll")
        telnet_client.send("cd /etc").send("ll")

        result = telnet_client.read_all()
        LOGGER.debug(result)
        telnet_client.disconnect()
