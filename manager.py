from observation import Observation


class Manager:
    """
        manages the activities of a server
    """

    def __init__(self):
        self.connections = []

    async def manage(self, server):
        await server.serve()
        await self.observe(server)
    
    async def observe(self, server):
        async for connection in Observation(server):
            self.connections.append(connection)
