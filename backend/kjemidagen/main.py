import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from kjemidagen.user import user_router
from kjemidagen.auth import auth_router
from kjemidagen.company import company_router
from kjemidagen.config import Config

app = FastAPI()

origins = ["https://kjemidagen.no", "https://www.kjemidagen.no"]
if Config.dev:
    origins += [
        "http://localhost:3000",
        "http://localhost:3001",
        "https://kjemidagen.localhost",
        "http://kjemidagen.localhost",
        "http://frontend",
        "http://caddy",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/v1/users", tags=["users"])
app.include_router(auth_router, prefix="/v1/auth", tags=["auth"])
app.include_router(company_router, prefix="/v1/companies", tags=["companies"])


@app.on_event("startup")
async def connect_to_db():
    logging.basicConfig(filename="kjemidagen.log", level=logging.INFO)


@app.get("/v1/")
async def assert_server_works():
    return ("Server is up", 200)
