from observation import Observation
import json


class Communicator:
    """
        listens for, transforms, and sends store messages to the client
    """

    def __init__(self, store):
        self.store = store

    async def communicate(self, client, connection_id):
        # TODO : implement client slice observation
        # and put the entire state tree into store
        # state = {'connections': {[id]: {'id'}}, ...}
        async for snapshot in Observation(self.store):
            await client.send(json.dumps({**snapshot, 'id': connection_id}))
