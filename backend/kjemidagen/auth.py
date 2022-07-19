import datetime
import os
import uuid
from dotenv import load_dotenv
from fastapi import APIRouter, Cookie, Request, status, HTTPException, Depends, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

from kjemidagen.crypto import verify_password
from kjemidagen.models import User, RefreshToken, TokenResponse


load_dotenv()
ACCESS_TOKEN_KEY = os.getenv("ACCESS_TOKEN_KEY")
REFRESH_TOKEN_KEY = os.getenv("REFRESH_TOKEN_KEY")
ALGORITHM = os.getenv("ALGORITHM") if not os.getenv("ALGORITHM") is None else "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, ACCESS_TOKEN_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = User.get(user_id)
    if user is None:
        raise credentials_exception
    return user

async def get_current_admin(current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=400, detail="Resource for admins only")

async def get_tokens(user: User):
    user_id = user.id.hex
    access_token_data = {
        "user_id": user_id,
        "is_admin": user.is_admin,
        "exp": datetime.datetime.utcnow()+datetime.timedelta(minutes=30)
    }
    access_token: str = jwt.encode(access_token_data, ACCESS_TOKEN_KEY, algorithm=ALGORITHM)

    refresh_token_in_db = RefreshToken()
    await refresh_token_in_db.create()
    
    refresh_token_data = {
        "user_id": user_id,
        "token_id": refresh_token_in_db.id.hex
    }
    refresh_token: str = jwt.encode(refresh_token_data, REFRESH_TOKEN_KEY, algorithm=ALGORITHM)

    return {"access_token": access_token, "refresh_token": refresh_token}

auth_router = APIRouter()

@auth_router.post("/login", response_model=TokenResponse)
async def login_for_refresh_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.find_one(User.username==form_data.username)
    if user is None: 
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not verify_password(plaintext_password= form_data.password, hashed_password= user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    tokens = await get_tokens(user)
    ## Set refresh token
    response.set_cookie(key="refresh", value=tokens["refresh_token"], max_age=60*60*24*30, httponly=True)#, path="/v1/auth")
    return TokenResponse(email=user.username, access_token=tokens["access_token"])

@auth_router.post("/token", response_model=TokenResponse)
async def refresh_access_token(response: Response, refresh_token: str | None = Cookie(default=None, alias="refresh")): 
    try:
        old_token: dict = jwt.decode(refresh_token, REFRESH_TOKEN_KEY, algorithms=[ALGORITHM])
        user_id: int = old_token.get("user_id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    except AttributeError:
        raise credentials_exception
    
    # Check if token already has been used
    old_token_in_db: RefreshToken = await RefreshToken.get(uuid.UUID(old_token.get("token_id")))
    if old_token_in_db.is_revoked:
        raise credentials_exception

    # Mark token as used
    await old_token_in_db.set({RefreshToken.is_revoked: True})

    user = await User.get(user_id)
    tokens = await get_tokens(user)
    ## Set refresh token
    response.set_cookie(key="refresh", value=tokens["refresh_token"], max_age=60*60*24*30, httponly=True) #, path="/v1/auth")
    return TokenResponse(email=user.username, access_token=tokens["access_token"])


@auth_router.post("/logout")
async def logout(response: Response, refresh_token: str | None = Cookie(default=None, alias="refresh")):
    try:
        old_token: dict = jwt.decode(refresh_token, REFRESH_TOKEN_KEY, algorithms=[ALGORITHM])
        user_id: int = old_token.get("user_id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # Check if token already has been used
    old_token_in_db: RefreshToken = await RefreshToken.get(uuid.UUID(old_token.get("token_id")))
    if old_token_in_db.is_revoked:
        raise credentials_exception

    # Mark token as used
    await old_token_in_db.set({RefreshToken.is_revoked: True})
    response.delete_cookie(key="refresh") #, path="/v1/auth/token") # unsets the cookie
    return ("logged out", 200)
