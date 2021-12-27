from fastapi import FastAPI
from dotenv import load_dotenv

from kjemidagen.database import create_db_and_tables
from kjemidagen.user import user_router
from kjemidagen.auth import auth_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    load_dotenv()
    create_db_and_tables()

app.include_router(user_router, prefix="/v1/users")
app.include_router(auth_router, prefix="/v1/auth")
