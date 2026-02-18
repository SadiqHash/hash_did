from fastapi import APIRouter
from hash_did.engine.did import create_did

router = APIRouter(tags=["did"])


@router.post("/")
async def create(public_key: str):
    doc = await create_did(public_key)
    return {"did": doc.id}
