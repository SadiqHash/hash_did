import pytest
from hash_did.engine.did import create_did


@pytest.mark.asyncio
async def test_create_did():
    doc = await create_did("pubkey")
    assert doc.id.startswith("did:hash:")
