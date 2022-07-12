from fastapi import FastAPI

from kjemidagen.user import user_router
from kjemidagen.auth import auth_router
from kjemidagen.company import company_router
from kjemidagen.database import init_database

app = FastAPI()

app.include_router(user_router, prefix="/v1/users", tags=["users"])
app.include_router(auth_router, prefix="/v1/auth", tags=["auth"])
app.include_router(company_router, prefix="/v1/companies", tags=["companies"])

@app.on_event("startup")
async def connect_to_db():
    await init_database()

@app.get("/v1/")
async def assert_server_works():
    return ("Server is up", 200)
