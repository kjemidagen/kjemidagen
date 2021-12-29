import os
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("DBServer")
user = os.getenv("DBUser")
dbname = os.getenv("Database")
password = os.getenv("DBPassword")
port = os.getenv("DBPort")

DATABASE_URL = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{dbname}"

engine = create_async_engine(
    DATABASE_URL,
    echo=True, #Remember to turn this off when going to prod
    future=True
)

async def get_session():
    async with AsyncSession(engine) as session:
        try:
            yield session
        finally:
            await session.close()

# import all SQLModels which are tables in the database to get their metadata
from kjemidagen.company import Company
from kjemidagen.user import User
from kjemidagen.auth import RefreshToken

async def create_db_and_tables():
    """Only for testing"""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)