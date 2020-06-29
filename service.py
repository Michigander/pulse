class Service:
    """
        combines a manager and server
    """

    def __init__(self, manager, server):
        self.server = server
        self.manager = manager

    async def run(self):
        return await self.manager.manage(self.server)
    
