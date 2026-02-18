"""
Decentralized Identifier (DID) domain.
"""

from .manager import create_did
from .resolver import resolve_did
from .document import DIDDocument

__all__ = [
    "create_did",
    "resolve_did",
    "DIDDocument",
]
