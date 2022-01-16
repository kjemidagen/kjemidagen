from fastapi import FastAPI

from kjemidagen.user import user_router
from kjemidagen.auth import auth_router
from kjemidagen.company import company_router

app = FastAPI()

app.include_router(user_router, prefix="/v1/users", tags=["users"])
app.include_router(auth_router, prefix="/v1/auth", tags=["auth"])
app.include_router(company_router, prefix="/v1/companies", tags=["companies"])
