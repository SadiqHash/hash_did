import base64


def encode_payload(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode()
