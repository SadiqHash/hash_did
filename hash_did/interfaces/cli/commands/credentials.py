import typer

app = typer.Typer()


@app.command()
def issue():
    print("Credential issuance placeholder")
