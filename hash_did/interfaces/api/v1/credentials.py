from fastapi import APIRouter
from hash_did.engine.credentials import issue_credential

router = APIRouter(tags=["credentials"])


@router.post("/")
async def issue(issuer: str, subject: str, data: dict):
    vc = await issue_credential(issuer, subject, data)
    return {"issuer": vc.issuer, "subject": vc.subject}
