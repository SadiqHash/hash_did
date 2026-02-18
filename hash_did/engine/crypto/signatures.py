def sign(private_key, message: bytes) -> bytes:
    return private_key.sign(message)


def verify(public_key, message: bytes, signature: bytes) -> bool:
    try:
        public_key.verify(signature, message)
        return True
    except Exception:
        return False
