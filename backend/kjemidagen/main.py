from fastapi import FastAPI
from dotenv import load_dotenv

from kjemidagen.database import create_db_and_tables
from kjemidagen.user import user_router
from kjemidagen.auth import auth_router
from kjemidagen.company import company_router

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()

app.include_router(user_router, prefix="/v1/users", tags=["users"])
app.include_router(auth_router, prefix="/v1/auth", tags=["auth"])
app.include_router(company_router, prefix="/v1/companies", tags=["companies"])
