import asyncio
from pulse_server import PulseServer


if __name__ == "__main__":
    server = PulseServer()
    asyncio.get_event_loop().run_until_complete(server.serve())
    asyncio.get_event_loop().run_forever()
