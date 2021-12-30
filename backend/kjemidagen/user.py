from datetime import datetime
from sqlalchemy import func
from typing import TYPE_CHECKING, List, Optional
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel, Field, Relationship, Session
from sqlmodel.sql.expression import select

from kjemidagen.database import get_session
from kjemidagen.crypto import hash_password
from kjemidagen.auth import get_current_user, get_current_admin

from kjemidagen.models import User, UserCreate, UserCreateResponse, UserGetResponse, UserUpdate

if TYPE_CHECKING:
    from kjemidagen.company import Company

user_router = APIRouter()

@user_router.get("/", dependencies=[Depends(get_current_admin)], response_model=List[UserGetResponse])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(User))
    users: List[User] = result.all()
    if not users:
        raise HTTPException(status_code=404, detail="No users")
    return users

@user_router.get("/{user_id}")
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="No users")
    return user

@user_router.post("/")
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(User).filter_by(username=user.username))
    if result.one_or_none() != None:
        raise HTTPException(status_code=409, detail="Username already taken")
    user = User(username=user.username, hashed_password=hash_password(password=user.password))
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return UserCreateResponse.from_orm(user)

@user_router.patch("/{user_id}")
async def edit_user(user_id: int, updated_user: UserUpdate, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    updated_data = updated_user.dict(exclude_unset=True) # get only the values which are not empty
    for field, value in updated_data.items():
        setattr(user, field, value)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return UserCreateResponse.from_orm(user)


@user_router.delete("/{user_id}")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await session.delete(user)
    await session.commit()
    return  {"ok": True }