"""
    Telnet client
"""

from telnetlib import Telnet
from typing import List

import logging
import time


class InvalidUserException(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class TelnetClient():
    """
        Telnet client
    """
    RESULT_TIMEOUT = 5
    ENCODE_TYPE = 'ascii'
    DECODE_TYPE = 'ascii'

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        # self.__is_incorrect_info: bool = False
        self.__telnet: Telnet

    def connect(self, host: str, user: str, password: str, time_out: int = 5):
        """ connect to telnet server """

        # try:
        self.__telnet = Telnet(host, port=23, timeout=time_out)

        # login
        self.read_until("login:")
        self.send(user)

        # password
        self.read_until("Password: ")
        self.send(password)
        result = self.read_until("{}@".format(user))

        if "Login incorrect" in result:
            raise InvalidUserException("Please check user or password.")

    def disconnect(self):
        """ disconnect the connection  """
        self.__telnet.write("exit".encode(self.ENCODE_TYPE) + b"\n")
        self.__telnet.close()
        self.logger.info("Successfully disconnected")

    def send(self, command: str):
        """ send command """
        encode_command = command.encode(self.ENCODE_TYPE) + b"\n"
        self.logger.debug("send command: %s", encode_command)
        self.__telnet.write(encode_command)
        return self

    def read_until(self, delimiter: str,
                   read_delay_time: float = 0.5) -> List[str]:
        """ read result """
        time.sleep(read_delay_time)

        tel_line: str = self.__telnet.read_until(
            delimiter.encode(self.ENCODE_TYPE),
            timeout=self.RESULT_TIMEOUT).decode()
        result: List[str] = tel_line.split('\r\n')
        self.logger.debug("read_until: %s", result)
        return result

    def read_all(self, read_delay_time: float = 0.5) -> List[str]:
        """ get data """
        time.sleep(read_delay_time)

        result: bytes = self.__telnet.read_very_eager()
        return result.decode().replace("\r", "").split('\n')
