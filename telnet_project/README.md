Python Telnet Test

1. tool : vs code
2. python version : 3.6

    ``` python
        host = "192.168.0.4"
        user = "test1233"
        password = "testdlqslek."
        telnet_client = TelnetClient()
        is_connected = telnet_client.connect(host, user, password)
        self.assertTrue(is_connected)

        telnet_client.send("cd /etc").send("ll")

        result = telnet_client.read_all()
        print(result)
        LOGGER.debug(result)

        self.assertTrue(telnet_client.is_connected)
        telnet_client.disconnect()
        self.assertTrue(not telnet_client.is_connected)
    ```