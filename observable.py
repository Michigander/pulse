import asyncio


class Observable:
    def __init__(self):
        self.future = asyncio.get_running_loop().create_future()

    def notify(self, state):
        self.future.set_result(state)
        self.future = asyncio.get_running_loop().create_future()
