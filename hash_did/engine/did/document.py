from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class DIDDocument:
    id: str
    public_key: str
    created: datetime
