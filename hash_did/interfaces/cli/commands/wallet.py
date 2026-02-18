import typer

app = typer.Typer()


@app.command()
def info():
    print("Wallet info placeholder")
