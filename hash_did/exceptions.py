class HashDIDException(Exception):
    """Base exception."""
    pass


class CryptoError(HashDIDException):
    pass


class DIDError(HashDIDException):
    pass


class WalletError(HashDIDException):
    pass


class VerificationError(HashDIDException):
    pass
