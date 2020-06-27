import asyncio
import websockets
import json


class WebsocketServer:

    def __init__(self):
        self.host = 'localhost'
        self.port = 5432
        self.websocket = None

    def serve(self):
        return websockets.serve(self.serve_loop, self.host, self.port)

    async def serve_loop(self, websocket, path):
        self.websocket = websocket
        async for message in websocket:
            await self.on_receive(message)

    def on_receive(self, message):
        # implement me
        pass


class PulseServer(WebsocketServer):

    def __init__(self):
        super().__init__()
        self.clients = []

    async def on_receive(self, raw_message):
        message = json.loads(raw_message)
        print(f'[log] received: {message}')

        if message['type'] == 'connect':
            await self.on_connect(message)

    async def on_connect(self, message):
        client_id = len(self.clients) + 1
        self.clients.append(client_id)
        await self.websocket.send(f'YEETster #{client_id}')


if __name__ == "__main__":
    server = PulseServer()
    asyncio.get_event_loop().run_until_complete(server.serve())
    asyncio.get_event_loop().run_forever()
