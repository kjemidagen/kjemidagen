import pytest
from sqlalchemy.sql.expression import null

from sqlmodel.ext.asyncio.session import AsyncSession
from httpx import AsyncClient

from kjemidagen.user import User
from kjemidagen.crypto import hash_password

from .conftest import session_fixture, client_fixture

@pytest.mark.anyio
async def test_get_all(session: AsyncSession, client: AsyncClient):
    created_user = User(username="testuser", hashed_password=hash_password("password123"))
    session.add(created_user)
    await session.commit()
    await session.refresh(created_user)

    response = await client.get(f"/v1/users/")
    data = response.json()

    assert response.status_code == 200
    assert data is not None

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

@pytest.mark.anyio
async def test_create_user(session: AsyncSession, client: AsyncClient):
    response = await client.post(
        "/v1/users/",
        json={
            "username": "bucky",
            "password": "kjemidagen22"
        })
    data = response.json()

    assert response.status_code == 200
    assert data["id"] is not None
    assert data["username"] == "bucky"
    assert data["is_admin"] is not None

    user = await session.get(User, data["id"])
    assert user.username == data["username"]

@pytest.mark.anyio
async def test_post_bad_schema(client: AsyncClient):
    response = await client.post(
        "/v1/users/",
        json={
            "username": "no password"
        })
    assert response.status_code == 422


@pytest.mark.anyio
async def test_patch(session: AsyncSession, client: AsyncClient):
    user = User(username="ricky", hashed_password=hash_password("morty2"), is_admin=False)
    session.add(user)
    await session.commit()
    await session.refresh(user)

    response = await client.patch(
        f"/v1/users/{user.id}",
        json={
            "is_admin": "True"
        })
    data = response.json()

    assert response.status_code == 200
    assert data["username"] == "ricky"
    assert data["is_admin"] == True

@pytest.mark.anyio
async def test_delete(session: AsyncSession, client: AsyncClient):
    user = User(username="hanschristian", hashed_password=hash_password("linjeforening"))
    session.add(user)
    await session.commit()
    await session.refresh(user)

    assert user.id is not None

    response = await client.delete(f"/v1/users/{user.id}")

    assert response.status_code == 200

    user_in_db = await session.get(User, user.id)
    
    assert user_in_db is None
