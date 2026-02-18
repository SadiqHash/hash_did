import json


async def export_wallet(data: dict) -> str:
    return json.dumps(data)


async def import_wallet(payload: str) -> dict:
    return json.loads(payload)
