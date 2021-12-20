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
    company: Optional["Company"] = Relationship(back_populates="user")
    is_admin: bool = False
    created_at: Optional[datetime] = Field(sa_column_kwargs={"server_default": func.now()})
    updated_at: Optional[datetime] = Field(sa_column_kwargs={"server_default": func.now(), "server_onupdate": func.now()})

class UserCreate(UserBase):
    pass

class UserGet(UserBase):
    is_admin: bool

user_router = APIRouter()

@user_router.get("/")
async def getUsers(session: AsyncSession = Depends(get_session)):
    users = session.get(User)
    if not users:
        raise HTTPException(status_code=404, detail="No users")
    return users

@user_router.get("/{id}")
async def getUsers(id: int, session: AsyncSession = Depends(get_session)):
    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="No users")
    return user

@user_router.post("/")
async def createUser(user: UserCreate, session: AsyncSession = Depends(get_session)):
    user = User(username=user.username)
    session.add(user)
    await session.commit()
    await session.refresh()
    return User