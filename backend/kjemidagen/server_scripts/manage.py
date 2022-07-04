from kjemidagen.models import User
from kjemidagen.crypto import hash_password
from kjemidagen.database import init_database
from getpass import getpass
import re
import asyncio

async def _create_initial_user(email: str, password: str):
    new_user = User(username=email, hashed_password=hash_password(password=password), )
    await new_user.insert()
    print("Success, user created")

async def _validate_email(email: str):
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    if not re.fullmatch(email_regex, email):
        print(f"\"{email}\" is not an email.")
        return False
    check_if_taken = await User.find(User.username==email).to_list()
    if len(check_if_taken) > 0:
        print(f"Email \"{email}\" is taken.")
        return False
    return True

async def main():
    await init_database()
    # Get email
    while True:
        print("Email: ", end="")
        email = input().strip().lower()
        if _validate_email: 
            break
    # Get password
    while True:
        password = getpass(prompt="Password: ")
        rep_password = getpass(prompt="Repeat password: ")
        if password == rep_password:
            break
        else:
            print("Passwords dont match")
    await _create_initial_user(email, password)

if __name__ == "__main__":
    asyncio.run(main())
