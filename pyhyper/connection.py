import socket

from .object import HyperliteObject


class Connection(socket.socket):
    def __init__(self, host, port, db_name):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.db_name = db_name

    def connect(self, **kwargs) -> bool:
        try:
            super().connect((self.host, self.port))
            print("[$] Connected to Hyperlite Database ..")
            return True
        except Exception as ex:
            raise ConnectionError(ex)

    def sendRequest(self, data: HyperliteObject):
        super().send(str(data).encode('UTF-8'))
        response = super().recv(4096).decode('UTF-8')
        return response

    def close(self):
        try:
            super().close()
        except Exception as ex:
            raise ConnectionError(ex)
        return True