Python Telnet Test

1. tool : vs code
2. python version : 3.6

    ``` python
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
    ```