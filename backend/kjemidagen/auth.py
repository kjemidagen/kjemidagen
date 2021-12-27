import datetime
import os
import uuid
from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlmodel import SQLModel, Field, Optional
from sqlmodel.ext.asyncio.session import AsyncSession

from kjemidagen.database import get_session
from kjemidagen.user import User

class RefreshToken(SQLModel):
    token_id: Optional[uuid.UUID] = Field(default=uuid.uuid4(), primary_key=True)
    is_revoked: bool = False

ACCESS_TOKEN_KEY = os.getenv("ACCESS_TOKEN_KEY")
REFRESH_TOKEN_KEY = os.getenv("REFRESH_TOKEN_KEY")
ALGORITHM = os.getenv("ALGORITHM") if not os.getenv("ALGORITHM") is None else "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(hashed_password: str) -> bool:
    return pwd_context.verify(hashed_password)

async def verify_access_token(token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, ACCESS_TOKEN_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await session.get(User, user_id=user_id)
    if user is None:
        raise credentials_exception
    return user

async def get_tokens(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, user_id)
    access_token_data = {
        "user_id": user.id,
        "is_admin": user.is_admin,
        "exp": datetime.datetime.utcnow()+datetime.timedelta(minutes=30)
    }
    access_token = jwt.encode(access_token_data, ACCESS_TOKEN_KEY, algorithm=ALGORITHM)

    refresh_token_data = {
        "user_id": user.id,
        "token_id": uuid.uuid4
    }
    refresh_token = jwt.encode(refresh_token_data, REFRESH_TOKEN_KEY, algorithm=ALGORITHM)

    return {"access_token": access_token, "refresh_token": refresh_token}

auth_router = APIRouter()

@auth_router.post("/login")
async def login_for_refresh_token(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)):
    user = await session.get(User, form_data.username)
    if user.id is None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not verify_password(form_data.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return await get_tokens(user.id)

@auth_router.post("/token")
async def refresh_access_token(refresh_token: str, session: AsyncSession = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        old_token: str = jwt.decode(refresh_token, REFRESH_TOKEN_KEY, algorithms=[ALGORITHM])
        user_id: int = old_token.get("user_id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # Check if token already has been used
    old_token_in_db: RefreshToken = await session.get(RefreshToken, old_token.get("token_id"))
    if old_token_in_db.is_revoked:
        raise credentials_exception

    # Mark token as used
    old_token_in_db.is_revoked = True
    await session.update(old_token_in_db)

    return await get_tokens(user_id)
