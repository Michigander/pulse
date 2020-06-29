import websockets

from connection import Connection
from observable import Observable


class Server(Observable):
    """
      generates connections (applications of interpreters
      and communicators over an interface)
    """

    def __init__(self, host, port, interpreter, communicator):
        super().__init__()
        self.host = host
        self.port = port
        self.interpreter = interpreter
        self.communicator = communicator

    def serve(self):
        print(f'[srvr] serving {self.host} {self.port}')
        return websockets.serve(self.serve_client, self.host, self.port)

    async def serve_client(self, websocket, path):
        print(f'[srvr] connection established')
        connection = Connection(
          websocket,
          self.interpreter,
          self.communicator
        )
        
        self.notify(connection)

        done, pending = await connection.connect()

        for task in pending:
            task.cancel()

        print(f'[srvr] connection closed')
