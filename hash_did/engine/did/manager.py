import uuid
from datetime import datetime
from .document import DIDDocument


async def create_did(public_key: str) -> DIDDocument:
    did = f"did:hash:{uuid.uuid4()}"
    return DIDDocument(
        id=did,
        public_key=public_key,
        created=datetime.utcnow(),
    )
