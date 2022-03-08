# import pytest

# from httpx import AsyncClient

# from kjemidagen.user import User
# from kjemidagen.crypto import hash_password

# @pytest.mark.anyio
# async def test_login(client: AsyncClient):
#     created_user = User(username="test@user.com", hashed_password=hash_password("hunter2"))
#     await created_user.insert()

#     response = await client.post(
#         "/v1/auth/login",
#         data={
#             "username": "test@user.com",
#             "password": "hunter2"
#         })
#     data = response.json()

#     assert response.status_code == 200
#     assert data["refresh_token"] is not None
#     assert data["access_token"] is not None
#     assert data["access_token"] != data["refresh_token"]

# @pytest.mark.anyio
# async def test_refresh(client: AsyncClient):
#     created_user = User(username="test@user.com", hashed_password=hash_password("hunter2"))
#     await created_user.insert()

#     login_response = await client.post(
#         "/v1/auth/login",
#         data={
#             "username": "test@user.com",
#             "password": "hunter2"
#         })
#     login_tokens = login_response.json()

#     refresh_response = await client.post(
#         "/v1/auth/token",
#         json={
#             "refresh_token": login_tokens["refresh_token"]
#         })
#     refreshed_tokens = refresh_response.json()

#     assert refresh_response.status_code == 200
#     assert refreshed_tokens["refresh_token"] is not None
#     assert refreshed_tokens["access_token"] is not None

# @pytest.mark.anyio
# async def test_refresh_theft(client: AsyncClient):
#     created_user = User(username="test@user.com", hashed_password=hash_password("hunter2"))
#     await created_user.insert()

#     login_response = await client.post(
#         "/v1/auth/login",
#         data={
#             "username": "test@user.com",
#             "password": "hunter2"
#         })
#     login_tokens = login_response.json()

#     await client.post(
#         "/v1/auth/token",
#         json={
#             "refresh_token": login_tokens["refresh_token"]
#         })
    
#     stolen_refresh_response = await client.post(
#         "/v1/auth/token",
#         json={
#             "refresh_token": login_tokens["refresh_token"]
#         })

#     assert stolen_refresh_response.status_code == 401