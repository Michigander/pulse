import json
from websocket_server import WebsocketServer


class PulseServer(WebsocketServer):

    def __init__(self):
        super().__init__()

    async def on_receive(self, connection_id, raw_message):
        message = json.loads(raw_message)
        print(f'[log] received: {message} on {connection_id}')

        if message['type'] == 'connect':
            await self.on_connect(connection_id, message)

    async def on_connect(self, connection_id, message):
        connection = self.connections[connection_id]
        await connection['websocket'].send(f'YEETster #{connection_id}')
