import os
from beanie import init_beanie, Document
import motor.motor_asyncio
from dotenv import load_dotenv
from kjemidagen.models import User, RefreshToken, Company

load_dotenv()
host = os.getenv("DBServer")
user = os.getenv("DBUser")
password = os.getenv("DBPassword")
port = os.getenv("DBPort")

DATABASE_URL = f"mongodb://{user}:{password}@{host}:{port}"

async def init_database():
    client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
    await init_beanie(database=client.db_name, document_models=[User, Company, RefreshToken])
