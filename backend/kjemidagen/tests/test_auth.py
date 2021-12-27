import pytest

from sqlmodel.ext.asyncio.session import AsyncSession
from httpx import AsyncClient

from kjemidagen.user import User
from kjemidagen.auth import hash_password

from .conftest import session_fixture, client_fixture

@pytest.mark.anyio
async def test_login(session: AsyncSession, client: AsyncClient):
    created_user = User(username="testuser", hashed_password=hash_password("hunter2"))
    session.add(created_user)
    await session.commit()
    await session.refresh(created_user)

    response = await client.post(
        "/v1/auth/login",
        json={
            "username": "testuser",
            "password": "hunter2"
        }
    )
    data = response.json()

    assert response.status_code == 200
    assert data["refresh_token"] is not None
    assert data["access_token"] is not None
    assert data["access_token"] != data["refresh_token"]
