import websockets
from datetime import datetime


class WebsocketServer:

    def __init__(self):
        self.host = 'localhost'
        self.port = 5432
        self.websocket = None
        self.connections = {}

    def serve(self):
        return websockets.serve(self.serve_loop, self.host, self.port)

    async def serve_loop(self, websocket, path):
        connection_id = f'{datetime.now()}'
        self.connections[connection_id] = {
          'id': connection_id,
          'websocket': websocket,
          'is_open': True,
        }

        async for message in websocket:
            await self.on_receive(connection_id, message)

        self.connections[connection_id]['is_open'] = False
        
    def on_receive(self, connection_id, message):
        # implement me
        pass
