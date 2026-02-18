from fastapi import APIRouter
from .v1 import health, did, credentials

api_router = APIRouter()
api_router.include_router(health.router, prefix="/v1")
api_router.include_router(did.router, prefix="/v1/did")
api_router.include_router(credentials.router, prefix="/v1/credentials")
