from fastapi import FastAPI
from sqlalchemy.sql.functions import user

from kjemidagen.database import create_db_and_tables
from kjemidagen.user import user_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(user_router, prefix="/v1/users")
