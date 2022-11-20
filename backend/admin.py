import typer
import asyncio
from server_scripts.create_initial_user import main as _create_initial_user

app = typer.Typer()


@app.command()
def create_initial_user():
    """Interactively create initial user"""
    asyncio.run(_create_initial_user())


@app.callback()
def cally():
    """Only exists to force other command to be named. If adding more commands, remove this"""
    pass


if __name__ == "__main__":
    app()
