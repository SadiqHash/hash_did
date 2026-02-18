from hash_did.engine.qr import encode_payload, decode_payload


def test_qr_roundtrip():
    data = b"hello"
    encoded = encode_payload(data)
    decoded = decode_payload(encoded)
    assert decoded == data
