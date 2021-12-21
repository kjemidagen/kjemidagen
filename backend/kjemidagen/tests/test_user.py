import pytest

from sqlmodel.ext.asyncio.session import AsyncSession
from httpx import AsyncClient

from kjemidagen.user import User
from kjemidagen.auth import hash_password

from .conftest import session_fixture, client_fixture

@pytest.mark.anyio
async def test_get(session: AsyncSession, client: AsyncClient):
    created_user = User(username="testuser", hashed_password=hash_password("password123"))
    session.add(created_user)
    await session.commit()
    await session.refresh(created_user)

    response = await client.get(f"/v1/users/{created_user.id}")
    data = response.json()

    assert response.status_code == 200
    assert data["username"] == "testuser"

async def test_post(session: AsyncSession, client: AsyncClient):
    assert 1 == 1