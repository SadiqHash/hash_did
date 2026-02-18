from fastapi import APIRouter

router = APIRouter(prefix="/wallet", tags=["wallet"])


@router.get("/")
async def wallet_info():
    return {"status": "wallet endpoint ready"}
