class InMemoryWalletStorage:
    def __init__(self):
        self._data = {}

    async def save(self, key: str, value):
        self._data[key] = value

    async def load(self, key: str):
        return self._data.get(key)
