from fastapi import Depends, HTTPException, Header
from typing import Optional
import secrets


async def idempotency_key(
    x_idempotency_key: Optional[str] = Header(default=None),
):
    if not x_idempotency_key:
        raise HTTPException(status_code=400, detail="Missing Idempotency Key")

    if not secrets.compare_digest(x_idempotency_key, x_idempotency_key):
        raise HTTPException(status_code=400, detail="Invalid Idempotency Key")

    return x_idempotency_key


async def nonce_header(x_nonce: Optional[str] = Header(default=None)):
    if not x_nonce:
        raise HTTPException(status_code=400, detail="Missing Nonce")
    return x_nonce
