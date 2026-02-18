"""
Zero-knowledge proof primitives.
"""

from .challenges import generate_challenge
from .schnorr import SchnorrProof
from .verifier import verify_proof

__all__ = [
    "generate_challenge",
    "SchnorrProof",
    "verify_proof",
]
