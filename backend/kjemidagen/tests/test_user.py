# import pytest

# from httpx import AsyncClient

# from kjemidagen.user import User
# from kjemidagen.crypto import hash_password

# @pytest.mark.anyio
# async def test_get_all(client: AsyncClient, admin_access_token):
#     created_user = User(username="test@user.com", hashed_password=hash_password("password123"))
#     await created_user.insert()

#     response = await client.get(f"/v1/users/",
#     headers={
#             "Authorization": "Bearer " + admin_access_token
#         })
#     data = response.json()

#     assert response.status_code == 200
#     assert data is not None

# @pytest.mark.anyio
# async def test_get(client: AsyncClient, admin_access_token):
#     created_user = User(username="test@user.com", hashed_password=hash_password("password123"))
#     await created_user.insert()

#     response = await client.get(f"/v1/users/{created_user.id}",
#     headers={
#             "Authorization": "Bearer " + admin_access_token
#         })
#     data = response.json()

#     assert response.status_code == 200
#     assert data["username"] == "test@user.com"

# @pytest.mark.anyio
# async def test_create_user(client: AsyncClient, admin_access_token):
#     response = await client.post(
#         "/v1/users/",
#         json={
#             "username": "test2@user.com",
#             "password": "kjemidagen22"
#         },
#         headers={
#             "Authorization": "Bearer " + admin_access_token
#         })
#     data = response.json()

#     assert response.status_code == 200
#     assert data["id"] is not None
#     assert data["username"] == "test2@user.com"
#     assert data["is_admin"] is not None

#     user = await User.get(data["id"])
#     assert user.username == data["username"]

# @pytest.mark.anyio
# async def test_post_bad_schema_no_password(client: AsyncClient, admin_access_token):
#     response = await client.post(
#         "/v1/users/",
#         json={
#             "username": "no@password.com",
#         },
#         headers={
#             "Authorization": "Bearer " + admin_access_token
#         })
#     assert response.status_code == 422

# @pytest.mark.anyio
# async def test_email_stripping(client: AsyncClient, admin_access_token):
#     response = await client.post(
#         "/v1/users/",
#         json={
#             "username": " spaces@inemail.com ",
#             "password": "kjemidagen22"
#         },
#         headers={
#             "Authorization": "Bearer " + admin_access_token
#         })
    
#     assert response.status_code == 200
#     user_id = response.json()["id"]
#     user_in_db = await User.get(user_id)
#     assert user_in_db.username == " spaces@inemail.com ".strip()

# @pytest.mark.anyio
# async def test_patch(client: AsyncClient, admin_access_token):
#     user = User(username="test@user.com", hashed_password=hash_password("morty2"), is_admin=False)
#     await user.insert()

#     response = await client.patch(
#         f"/v1/users/{user.id}",
#         json={
#             "is_admin": "True"
#         },
#         headers={
#             "Authorization": "Bearer " + admin_access_token
#         })
#     data = response.json()

#     assert response.status_code == 200
#     assert data["username"] == "test@user.com"
#     assert data["is_admin"] == True

# @pytest.mark.anyio
# async def test_delete(client: AsyncClient, admin_access_token):
#     user = User(username="test@user.com", hashed_password=hash_password("linjeforening"))
#     await user.insert()

#     assert user.id is not None

#     response = await client.delete(
#         f"/v1/users/{user.id}",
#         headers={
#             "Authorization": "Bearer " + admin_access_token
#         })

#     assert response.status_code == 200

#     user_in_db = await User.get(user.id)
    
#     assert user_in_db is None
