import pytest
from hash_did.engine.credentials import issue_credential


@pytest.mark.asyncio
async def test_issue_credential():
    vc = await issue_credential("issuer", "subject", {"name": "Hash"})
    assert vc.issuer == "issuer"
