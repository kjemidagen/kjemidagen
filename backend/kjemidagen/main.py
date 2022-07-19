from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from kjemidagen.user import user_router
from kjemidagen.auth import auth_router
from kjemidagen.company import company_router
from kjemidagen.database import init_database

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://www.kjemidagen.no",
    "https://kjemidagen.no",
    "http://frontend"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user_router, prefix="/v1/users", tags=["users"])
app.include_router(auth_router, prefix="/v1/auth", tags=["auth"])
app.include_router(company_router, prefix="/v1/companies", tags=["companies"])

@app.on_event("startup")
async def connect_to_db():
    await init_database()

@app.get("/v1/")
async def assert_server_works():
    return ("Server is up", 200)
