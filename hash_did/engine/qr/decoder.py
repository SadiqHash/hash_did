import base64


def decode_payload(data: str) -> bytes:
    return base64.urlsafe_b64decode(data.encode())
