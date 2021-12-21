from datetime import datetime
from sqlalchemy import func
from typing import TYPE_CHECKING, Optional
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel, Field, Relationship, Session
from sqlmodel.sql.expression import select

from kjemidagen.database import get_session
from kjemidagen.auth import hash_password

if TYPE_CHECKING:
    from kjemidagen.company import Company


class UserBase(SQLModel):
    username: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    company: Optional["Company"] = Relationship(back_populates="user")
    is_admin: bool = False
    created_at: Optional[datetime] = Field(sa_column_kwargs={"server_default": func.now()})
    updated_at: Optional[datetime] = Field(sa_column_kwargs={"server_default": func.now(), "server_onupdate": func.now()})

class UserCreate(UserBase):
    password: str

class UserGet(UserBase):
    is_admin: bool

class UserUpdate(SQLModel):
    is_admin: Optional[bool]

user_router = APIRouter()

@user_router.get("/")
async def get_users(session: AsyncSession = Depends(get_session)):
    users = await session.get(User)
    if not users:
        raise HTTPException(status_code=404, detail="No users")
    return users

@user_router.get("/{id}")
async def get_user(id: int, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="No users")
    return user

@user_router.post("/")
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    user = User(username=user.username, hashed_password=hash_password(password=user.password))
    session.add(user)
    await session.commit()
    await session.refresh()
    return User

@user_router.put("/{user_id}")
async def edit_user(user_id: int, updated_user: UserUpdate, session: AsyncSession = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    updated_data = updated_user.dict(exclude_unset=True) # get only the values which are not empty
    for field, value in updated_data.items():
        setattr(user, field, value)
    await session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


@user_router.delete("/{user_id}")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return  {"ok": True }