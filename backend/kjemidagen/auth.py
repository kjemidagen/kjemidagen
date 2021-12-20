from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

auth_router = APIRouter()

@auth_router.get("/login")
async def login():
    pass


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(hashed_password: str) -> bool:
    return pwd_context.verify(hashed_password)
