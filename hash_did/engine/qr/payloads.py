from dataclasses import dataclass


@dataclass
class QRPayload:
    type: str
    data: str
