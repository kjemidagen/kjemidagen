import datetime
import os
import uuid
from dotenv import load_dotenv
from fastapi import APIRouter, status, HTTPException, Depends, Body
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlmodel import SQLModel, Field, select
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import Optional

from kjemidagen.database import get_session
from kjemidagen.user import User
from kjemidagen.crypto import verify_password

class RefreshToken(SQLModel, table=True):
    token_id: Optional[uuid.UUID] = Field(default=uuid.uuid4(), primary_key=True)
    is_revoked: bool = False

load_dotenv()
ACCESS_TOKEN_KEY = os.getenv("ACCESS_TOKEN_KEY")
REFRESH_TOKEN_KEY = os.getenv("REFRESH_TOKEN_KEY")
ALGORITHM = os.getenv("ALGORITHM") if not os.getenv("ALGORITHM") is None else "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_session)):
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
    user = await session.get(User, user_id)
    if user is None:
        raise credentials_exception
    return user

async def get_current_admin(current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=400, detail="Resource for admins only")

async def get_tokens(user: User, session: AsyncSession):
    access_token_data = {
        "user_id": user.id,
        "is_admin": user.is_admin,
        "exp": datetime.datetime.utcnow()+datetime.timedelta(minutes=30)
    }
    access_token = jwt.encode(access_token_data, ACCESS_TOKEN_KEY, algorithm=ALGORITHM)

    refresh_token_id: uuid.UUID = uuid.uuid4()
    refresh_token_data = {
        "user_id": user.id,
        "token_id": refresh_token_id.hex
    }
    refresh_token = jwt.encode(refresh_token_data, REFRESH_TOKEN_KEY, algorithm=ALGORITHM)

    session.add(RefreshToken(token_id=refresh_token_id))
    await session.commit()

    return {"access_token": access_token, "refresh_token": refresh_token}

auth_router = APIRouter()

@auth_router.post("/login")
async def login_for_refresh_token(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)):
    query = select(User).filter_by(username=form_data.username)
    results = await session.exec(query)
    user: User = results.one_or_none()
    if user.id is None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not verify_password(plaintext_password= form_data.password, hashed_password= user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return await get_tokens(user, session)

@auth_router.post("/token")
async def refresh_access_token(session: AsyncSession = Depends(get_session), refresh_token: str = Body(..., embed=True)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        old_token: dict = jwt.decode(refresh_token, REFRESH_TOKEN_KEY, algorithms=[ALGORITHM])
        user_id: int = old_token.get("user_id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # Check if token already has been used
    old_token_in_db: RefreshToken = await session.get(RefreshToken, uuid.UUID(old_token.get("token_id")))
    if old_token_in_db.is_revoked:
        raise credentials_exception

    # Mark token as used
    # TODO: possibly mark all tokens from this user as revoked
    old_token_in_db.is_revoked = True
    # setattr(old_token_in_db, "is_revoked", True) # "old_token_in_db.is_revoked = True" is not allowed
    session.add(old_token_in_db)
    await session.commit()

    user = await session.get(User, user_id)
    return await get_tokens(user, session)
