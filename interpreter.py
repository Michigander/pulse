import json


class Interpreter:
    """
        listens for, transforms, and sends client messages to the back end
    """

    def __init__(self, store):
        self.store = store

    async def interpret(self, client, connection_id):
        async for message_str in client:
            message = json.loads(message_str)
            self.store.send(message, connection_id)
