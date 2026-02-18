import pytest
from hash_did.wallet.keystore import InMemoryKeyStore


@pytest.mark.asyncio
async def test_keystore():
    store = InMemoryKeyStore()
    await store.save("id", "key")
    assert await store.load("id") == "key"
