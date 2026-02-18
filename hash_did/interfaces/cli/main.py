import typer

app = typer.Typer()


@app.command()
def version():
    from hash_did import __version__
    print(__version__)


if __name__ == "__main__":
    app()
