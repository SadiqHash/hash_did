class InMemoryKeyStore:
    def __init__(self):
        self._store = {}

    async def save(self, key_id: str, key):
        self._store[key_id] = key

    async def load(self, key_id: str):
        return self._store.get(key_id)
