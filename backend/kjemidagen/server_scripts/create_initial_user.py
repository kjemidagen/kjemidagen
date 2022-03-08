import typer
from kjemidagen.models import User, UserCreate
from kjemidagen.crypto import hash_password

async def main(user: UserCreate):
    new_user = User(username=user.username, hashed_password=hash_password(password=user.password))
    await new_user.insert()

if __name__ == "__main__":
    typer.run(main)