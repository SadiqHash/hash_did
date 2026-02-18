from cryptography.hazmat.primitives.asymmetric import ed25519


def generate_keypair():
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key
