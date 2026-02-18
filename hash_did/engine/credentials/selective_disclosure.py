def disclose_fields(vc, fields: list[str]) -> dict:
    return {k: v for k, v in vc.data.items() if k in fields}
