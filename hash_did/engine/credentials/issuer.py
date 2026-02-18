from datetime import datetime
from .models import VerifiableCredential


async def issue_credential(issuer: str, subject: str, data: dict):
    return VerifiableCredential(
        issuer=issuer,
        subject=subject,
        issued_at=datetime.utcnow(),
        data=data,
    )
