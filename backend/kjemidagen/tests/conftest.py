import pytest
# import docker
# import motor.motor_asyncio
# from httpx import AsyncClient
# from beanie import init_beanie
# from kjemidagen.crypto import hash_password

# from kjemidagen.main import app
# from kjemidagen.database import init_database
# from kjemidagen.models import User, Company, RefreshToken

@pytest.fixture
def anyio_backend():
    return "asyncio"

# @pytest.fixture(autouse=True)
# async def database_fixture():
    
#     async def init_database_override():
#         docker_client = docker.from_env()
#         container = docker_client.containers.run("mongo", detach=True, ports={"27017/tcp":27017})   
#         db_client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
#         await init_beanie(database=db_client.db_name, document_models=[User, Company, RefreshToken])
#         yield None
        
#         container.stop()
#         container.remove()


#     app.dependency_overrides[init_database] = init_database_override
#     yield None

#     app.dependency_overrides.clear()

# @pytest.fixture(name="client")
# async def client_fixture():
#     async with AsyncClient(app=app, base_url="http://localhost:8007") as client:
#         yield client

# @pytest.fixture(name="admin_access_token")
# async def admin_fixture(client: AsyncClient):
#     admin_user = User(username="test@user.com", is_admin=True, hashed_password=hash_password("test@user.compw"))    
#     await admin_user.insert()

#     response = await client.post(
#         "/v1/auth/login",
#         data={
#             "username": "test@user.com",
#             "password": "test@user.compw"
#         })
#     data = response.json()

#     yield data["access_token"]
