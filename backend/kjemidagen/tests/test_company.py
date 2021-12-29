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
    assert data["password"] is not None
    assert data["username"] == "the_Zucc_96"

@pytest.mark.anyio
async def test_edit_company(client: AsyncClient, admin_access_token):
    res_1 = await client.post(
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
    created_company: dict = res_1.json()
    
    company_id = created_company.get('id')
    response = await client.patch(
        f"/v1/companies/{company_id}",
        json={
            "additional_data": "I am still human"
        },
        headers={
            "Authorization": "Bearer " + admin_access_token
        }
    )
    data = response.json()

    assert response.status_code == 200
    assert data["title"] == "Metagross TM"
    assert data["additional_data"] == "I am still human"

@pytest.mark.anyio
async def test_delete_company(client: AsyncClient, admin_access_token):
    res_1 = await client.post(
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
    created_company: dict = res_1.json()

    res_2 = await client.delete(
        f"/v1/users/{created_company.get('id')}",
        headers={
            "Authorization": "Bearer " + admin_access_token
        }
    )
    assert res_2.status_code == 200

    res_3 = await client.get(
        f"/v1/users/{created_company.get('id')}",
        headers={
            "Authorization": "Bearer " + admin_access_token
        }
    )
    assert res_3.status_code == 404