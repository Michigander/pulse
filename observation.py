import asyncio


class Observation:
    def __init__(self, observable):
        self.observable = observable

    def __aiter__(self):
        return self

    async def __anext__(self):
        return await asyncio.shield(self.observable.future)
