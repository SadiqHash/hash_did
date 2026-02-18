from dataclasses import dataclass
from functools import lru_cache
import os


@dataclass(frozen=True)
class Settings:
    app_name: str = "hash_did"
    environment: str = os.getenv("HASH_DID_ENV", "development")
    debug: bool = environment == "development"
    secret_key: str = os.getenv("HASH_DID_SECRET", "change-me")
    nonce_ttl_seconds: int = 300


@lru_cache
def get_settings() -> Settings:
    return Settings()
