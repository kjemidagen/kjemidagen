import pytest
from sqlmodel import SQLModel
from httpx import AsyncClient
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.pool import StaticPool
from kjemidagen.crypto import hash_password

from kjemidagen.main import app
from kjemidagen.database import get_session
from kjemidagen.user import User

@pytest.fixture
def anyio_backend():
    return "asyncio"

@pytest.fixture(name="session")
async def session_fixture():
    engine = create_async_engine(
        "sqlite+aiosqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    async with engine.begin() as conn:
        from kjemidagen.user import User
        from kjemidagen.company import Company
        await conn.run_sync(SQLModel.metadata.create_all)

    async with AsyncSession(engine) as session:
        yield session

@pytest.fixture(name="client")
async def client_fixture(session: AsyncSession):
    async def get_session_override():
        return session
    
    app.dependency_overrides[get_session] = get_session_override
    async with AsyncClient(app=app, base_url="http://localhost:8007") as client:
        yield client
    app.dependency_overrides.clear()

@pytest.fixture(name="admin_access_token")
async def admin_fixture(session: AsyncSession, client: AsyncClient):
    admin_user = User(username="testadmin", is_admin=True, hashed_password=hash_password("testadminpw"))    
    session.add(admin_user)
    await session.commit()

    response = await client.post(
        "/v1/auth/login",
        data={
            "username": "testadmin",
            "password": "testadminpw"
        })
    data = response.json()

    yield data["access_token"]
