from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class VerifiableCredential:
    issuer: str
    subject: str
    issued_at: datetime
    data: dict
