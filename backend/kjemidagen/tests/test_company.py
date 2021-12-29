import pytest
from sqlalchemy.sql.functions import user

from sqlmodel.ext.asyncio.session import AsyncSession
from httpx import AsyncClient

from kjemidagen.company import Company
from kjemidagen.user import User
from kjemidagen.crypto import hash_password

from .conftest import session_fixture, client_fixture

@pytest.mark.anyio
async def test_get_all(session: AsyncSession, client: AsyncClient, admin_access_token: str):
    created_user = User(username="companyuser", hashed_password=hash_password("etmegetsterktpassword123"))
    created_company = Company(
        title="Pengefirmaet",
        email_address="sjefen@pengefirmaet.no",
        number_of_representatives=2,
        additional_data="{}",
        user=created_user)
    session.add(created_user)
    session.add(created_company)
    await session.commit()

    response = await client.get(
        f"/v1/companies/",
        headers={
            "Authorization": "Bearer " + admin_access_token
        }
    )
    data = response.json()

    assert response.status_code == 200
    assert data is not None

@pytest.mark.anyio
async def test_get(session: AsyncSession, client: AsyncClient, admin_access_token):
    created_user = User(username="companyuser", hashed_password=hash_password("etmegetsterktpassword123"))
    created_company = Company(
        title="Pengefirmaet",
        email_address="sjefen@pengefirmaet.no",
        number_of_representatives=2,
        additional_data="{}",
        user=created_user)
    session.add(created_user)
    session.add(created_company)
    await session.commit()
    await session.refresh(created_user)
    await session.refresh(created_company)

    response = await client.get(
        f"/v1/companies/{created_user.id}",
        headers={
            "Authorization": "Bearer " + admin_access_token
        }
    )
    data = response.json()

    assert response.status_code == 200
    assert data["title"] == "Pengefirmaet"

@pytest.mark.anyio
async def test_create_company(client: AsyncClient, admin_access_token):
    response = await client.post(
        "/v1/companies/",
        json={
            "username": "the_Zucc_96",
            "title": "Metagross TM",
            "email_address": "marcus@berger.gov",
            "number_of_representatives": "2",
            "additional_data": "I am a human i swear"
        },
        headers={
            "Authorization": "Bearer " + admin_access_token
        }
    )
    data = response.json()

    assert response.status_code == 200
    assert data["hashed_password"] is not None
    assert data["is_admin"] == False
    assert data["username"] == "the_Zucc_96"

@pytest.mark.anyio
async def test_edit_company(session: AsyncSession, client: AsyncClient, admin_access_token):
    # TODO: test this mess
    assert 1 == 0
