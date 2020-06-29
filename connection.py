import asyncio
import uuid


class Connection:
    """
        interprets and communicates over an interface
    """
    
    def __init__(self, client, interpreter, communicator):
        self.interpreter = interpreter
        self.communicator = communicator
        self.client = client
        self.id = str(uuid.uuid4())

    async def connect(self):
        interpretation = asyncio.get_running_loop().create_task(
            self.interpreter.interpret(self.client, self.id)
        )

        communication = asyncio.get_running_loop().create_task(
            self.communicator.communicate(self.client, self.id)
        )

        return await asyncio.wait(
            [interpretation, communication],
            return_when=asyncio.FIRST_COMPLETED,
        )
