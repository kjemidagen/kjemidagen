# import pytest
# from httpx import AsyncClient

# from kjemidagen.company import Company
# from kjemidagen.user import User
# from kjemidagen.crypto import hash_password

# @pytest.mark.anyio
# async def test_get_all(client: AsyncClient, admin_access_token: str):
#     created_user = User(username="test@user.com", hashed_password=hash_password("etmegetsterktpassword123"))
#     created_company = Company(
#         title="Pengefirmaet",
#         public_email="sjefen@pengefirmaet.no",
#         number_of_representatives=2,
#         additional_data="{}",
#         user=created_user)
#     await created_user.insert()

#     response = await client.get(
#         f"/v1/companies/",
#         headers={
#             "Authorization": "Bearer " + admin_access_token
#         }
#     )
#     data = response.json()

#     assert response.status_code == 200
#     assert data is not None

# @pytest.mark.anyio
# async def test_get(client: AsyncClient, admin_access_token):
#     created_user = User(username="test@user.com", hashed_password=hash_password("etmegetsterktpassword123"))
#     created_company = Company(
#         title="Pengefirmaet",
#         public_email="sjefen@pengefirmaet.no",
#         number_of_representatives=2,
#         additional_data="{}",
#         user=created_user)
#     await created_user.insert()
#     await created_company.insert()

#     response = await client.get(
#         f"/v1/companies/{created_user.id}",
#         headers={
#             "Authorization": "Bearer " + admin_access_token
#         }
#     )
#     data = response.json()

#     assert response.status_code == 200
#     assert data["title"] == "Pengefirmaet"

# @pytest.mark.anyio
# async def test_create_company(client: AsyncClient, admin_access_token):
#     response = await client.post(
#         "/v1/companies/",
#         json={
#             "username": "test@user.com",
#             "title": "Metagross TM",
#             "public_email": "marcus@berger.gov",
#             "number_of_representatives": "2",
#             "additional_data": "I am a human i swear"
#         },
#         headers={
#             "Authorization": "Bearer " + admin_access_token
#         }
#     )
#     data = response.json()

#     assert response.status_code == 200
#     assert data["password"] is not None
#     assert data["username"] == "test@user.com"

# @pytest.mark.anyio
# async def test_edit_company(client: AsyncClient, admin_access_token):
#     res_1 = await client.post(
#         "/v1/companies/",
#         json={
#             "username": "test@user.com",
#             "title": "Metagross TM",
#             "public_email": "marcus@berger.gov",
#             "number_of_representatives": "2",
#             "additional_data": "I am a human i swear"
#         },
#         headers={
#             "Authorization": "Bearer " + admin_access_token
#         }
#     )
#     created_company: dict = res_1.json()
    
#     company_id = created_company.get('id')
#     response = await client.patch(
#         f"/v1/companies/{company_id}",
#         json={
#             "additional_data": "I am still human"
#         },
#         headers={
#             "Authorization": "Bearer " + admin_access_token
#         }
#     )
#     data = response.json()

#     assert response.status_code == 200
#     assert data["title"] == "Metagross TM"
#     assert data["additional_data"] == "I am still human"

# @pytest.mark.anyio
# async def test_delete_company(client: AsyncClient, admin_access_token):
#     res_1 = await client.post(
#         "/v1/companies/",
#         json={
#             "username": "test@user.com",
#             "title": "Metagross TM",
#             "public_email": "marcus@berger.gov",
#             "number_of_representatives": "2",
#             "additional_data": "I am a human i swear"
#         },
#         headers={
#             "Authorization": "Bearer " + admin_access_token
#         }
#     )
#     created_company: dict = res_1.json()

#     res_2 = await client.delete(
#         f"/v1/users/{created_company.get('id')}",
#         headers={
#             "Authorization": "Bearer " + admin_access_token
#         }
#     )
#     assert res_2.status_code == 200

#     res_3 = await client.get(
#         f"/v1/users/{created_company.get('id')}",
#         headers={
#             "Authorization": "Bearer " + admin_access_token
#         }
#     )
#     assert res_3.status_code == 404