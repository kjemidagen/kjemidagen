import typer
from ..models import User
from ..crypto import hash_password
from ..database import init_database
import re
import asyncio

app = typer.Typer()

async def _create_initial_user(email: str, password: str):
    new_user = User(username=email, hashed_password=hash_password(password=password))
    await new_user.insert()
    typer.echo("Success, user created")

async def _validate_username(email: str):
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    if not re.fullmatch(email_regex, email):
        raise typer.BadParameter(f"\"{email}\" not an email.")

    check_if_taken = await User.find(User.username==email).to_list()
    if len(check_if_taken) > 0:
        raise typer.BadParameter(f"Email \"{email}\" is taken.")

def validate_username(email: str):
    asyncio.run(_validate_username(email))

@app.command()
async def create_initial_user(email: str = typer.Option(..., prompt=True, callback=validate_username),
                                password: str = typer.Option(..., prompt=True, confirmation_prompt=True, hide_input=True)):
    asyncio.run(_create_initial_user(email, password))

if __name__ == "__main__":
    asyncio.run(init_database())
    app()