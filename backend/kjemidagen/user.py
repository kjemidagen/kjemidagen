from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel.sql.expression import select

from kjemidagen.database import get_session
from kjemidagen.crypto import hash_password
from kjemidagen.auth import get_current_user, get_current_admin

from kjemidagen.models import User, UserCreate, UserCreateResponse, UserGetResponse, UserUpdate, UserUpdateResponse

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

user_router = APIRouter()

@user_router.get("/", dependencies=[Depends(get_current_admin)], response_model=List[UserGetResponse])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(User))
    users: List[User] = result.all()
    if not users:
        raise HTTPException(status_code=404, detail="No users")
    return users

@user_router.get("/{user_id}", response_model=UserGetResponse)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session), current_user: User = Depends(get_current_user)):
    if not (current_user.is_admin or current_user.id == user_id):
        raise credentials_exception
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="No users")
    return user

@user_router.post("/", dependencies=[Depends(get_current_admin)], response_model=UserCreateResponse)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(User).filter_by(username=user.username))
    if result.one_or_none() != None:
        raise HTTPException(status_code=409, detail="Username already taken")
    user = User(username=user.username, hashed_password=hash_password(password=user.password))
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return UserCreateResponse.from_orm(user)

@user_router.patch("/{user_id}", response_model=UserUpdateResponse)
async def edit_user(user_id: int, updated_user: UserUpdate, session: AsyncSession = Depends(get_session), current_user: User = Depends(get_current_user)):
    if not (current_user.is_admin or current_user.id == user_id):
        raise credentials_exception
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    updated_data = updated_user.dict(exclude_unset=True) # get only the values which are not empty
    if "password" in updated_data.keys():
        hashed_password = hash_password(updated_data.pop("password"))
        setattr(user, "hashed_password", hashed_password)
    for field, value in updated_data.items():
        setattr(user, field, value)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return UserCreateResponse.from_orm(user)


@user_router.delete("/{user_id}", dependencies=[Depends(get_current_admin)])
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await session.delete(user)
    await session.commit()
    return  {"ok": True }