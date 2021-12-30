import datetime
import uuid
from sqlalchemy import func
from sqlmodel import SQLModel, Relationship, Field
from pydantic import EmailStr
from typing import Optional


class UserBase(SQLModel):
    username: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    company: Optional["Company"] = Relationship(back_populates="user", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    is_admin: bool = False
    created_at: Optional[datetime.datetime] = Field(sa_column_kwargs={"server_default": func.now()})
    updated_at: Optional[datetime.datetime] = Field(sa_column_kwargs={"server_default": func.now(), "server_onupdate": func.now()})

class UserCreate(UserBase):
    password: str

class UserCreateResponse(UserBase):
    """Contains fields returned on user creation"""
    id: int
    is_admin: bool

class UserGetResponse(UserBase):
    """Contains fields returned from get requests"""
    id: int
    is_admin: bool

class UserUpdate(SQLModel):
    """Contains fields which you can update"""
    is_admin: Optional[bool]


class CompanyBase(SQLModel):
    title: str
    email_address: EmailStr
    number_of_representatives: int
    additional_data: Optional[str]
    created_at: Optional[datetime.datetime] = Field(sa_column_kwargs={"server_default": func.now()})
    updated_at: Optional[datetime.datetime] = Field(sa_column_kwargs={"server_default": func.now(), "server_onupdate": func.now()})

class Company(CompanyBase, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True, foreign_key="user.id")
    user: "User" = Relationship(back_populates="company")

class CompanyAndUserCreate(CompanyBase, UserBase):
    pass

class CompanyCreateResponse(CompanyBase, UserBase):
    id: int
    password: str

class CompanyUpdate(SQLModel):
    title: Optional[str]
    email_address: Optional[EmailStr]
    number_of_representatives: Optional[int]
    additional_data: Optional[str]

class CompanyUpdateResponse(CompanyBase):
    id: int

class RefreshToken(SQLModel, table=True):
    token_id: Optional[uuid.UUID] = Field(default=uuid.uuid4().hex, primary_key=True)
    is_revoked: bool = False