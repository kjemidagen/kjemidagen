import pytest
from sqlalchemy.sql.expression import null

from sqlmodel.ext.asyncio.session import AsyncSession
from httpx import AsyncClient

from kjemidagen.user import User
from kjemidagen.crypto import hash_password

@pytest.mark.anyio
async def test_get_all(session: AsyncSession, client: AsyncClient, admin_access_token):
    created_user = User(username="testuser", hashed_password=hash_password("password123"))
    session.add(created_user)
    await session.commit()
    await session.refresh(created_user)

    response = await client.get(f"/v1/users/",
    headers={
            "Authorization": "Bearer " + admin_access_token
        })
    data = response.json()

    assert response.status_code == 200
    assert data is not None

@pytest.mark.anyio
async def test_get(session: AsyncSession, client: AsyncClient, admin_access_token):
    created_user = User(username="testuser", hashed_password=hash_password("password123"))
    session.add(created_user)
    await session.commit()
    await session.refresh(created_user)

    response = await client.get(f"/v1/users/{created_user.id}",
    headers={
            "Authorization": "Bearer " + admin_access_token
        })
    data = response.json()

    assert response.status_code == 200
    assert data["username"] == "testuser"

@pytest.mark.anyio
async def test_create_user(session: AsyncSession, client: AsyncClient, admin_access_token):
    response = await client.post(
        "/v1/users/",
        json={
            "username": "bucky",
            "password": "kjemidagen22"
        },
        headers={
            "Authorization": "Bearer " + admin_access_token
        })
    data = response.json()

    assert response.status_code == 200
    assert data["id"] is not None
    assert data["username"] == "bucky"
    assert data["is_admin"] is not None

    user = await session.get(User, data["id"])
    assert user.username == data["username"]

@pytest.mark.anyio
async def test_post_bad_schema(client: AsyncClient, admin_access_token):
    response = await client.post(
        "/v1/users/",
        json={
            "username": "no password"
        },
        headers={
            "Authorization": "Bearer " + admin_access_token
        })
    assert response.status_code == 422


@pytest.mark.anyio
async def test_patch(session: AsyncSession, client: AsyncClient, admin_access_token):
    user = User(username="ricky", hashed_password=hash_password("morty2"), is_admin=False)
    session.add(user)
    await session.commit()
    await session.refresh(user)

    response = await client.patch(
        f"/v1/users/{user.id}",
        json={
            "is_admin": "True"
        },
        headers={
            "Authorization": "Bearer " + admin_access_token
        })
    data = response.json()

    assert response.status_code == 200
    assert data["username"] == "ricky"
    assert data["is_admin"] == True

@pytest.mark.anyio
async def test_delete(session: AsyncSession, client: AsyncClient, admin_access_token):
    user = User(username="hanschristian", hashed_password=hash_password("linjeforening"))
    session.add(user)
    await session.commit()
    await session.refresh(user)

    assert user.id is not None

    response = await client.delete(
        f"/v1/users/{user.id}",
        headers={
            "Authorization": "Bearer " + admin_access_token
        })

    assert response.status_code == 200

    user_in_db = await session.get(User, user.id)
    
    assert user_in_db is None
