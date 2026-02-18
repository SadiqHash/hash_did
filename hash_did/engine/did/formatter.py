import json
from .document import DIDDocument


def to_json(doc: DIDDocument) -> str:
    return json.dumps(doc.__dict__, default=str)
