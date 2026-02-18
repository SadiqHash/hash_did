import typer
from hash_did.engine.did import create_did

app = typer.Typer()


@app.command()
def create(public_key: str):
    import asyncio
    doc = asyncio.run(create_did(public_key))
    print(doc.id)
