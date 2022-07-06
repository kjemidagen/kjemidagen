import datetime
import uuid
import pymongo
from beanie import Document, Indexed, Link, Insert, Replace, SaveChanges, before_event
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class User(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    username: Indexed(str, index_type=pymongo.TEXT, unique=True)
    hashed_password: str
    is_admin: bool = False
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    @before_event([Replace, SaveChanges])
    def set_updated_time(self):
        self.updated_at = datetime.datetime.now()
    class Settings:
        validate_on_save = True

class UserCreate(BaseModel):
    username: EmailStr
    password: str

class UserCreateResponse(BaseModel):
    """Contains fields returned on user creation"""
    username: EmailStr
    id: int
    is_admin: bool

class UserGetResponse(BaseModel):
    """Contains fields returned from get requests"""
    username: EmailStr
    id: int
    is_admin: bool

class UserUpdate(BaseModel):
    """Contains fields which you can update"""
    username: Optional[EmailStr]
    is_admin: Optional[bool]
    password: Optional[str]

class UserUpdateResponse(BaseModel):
    username: EmailStr
    id: int
    is_admin: bool

class Company(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    user: Link[User]
    title: Indexed(str)
    public_email: EmailStr
    number_of_representatives: int
    additional_data: Optional[str]
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    @before_event([Replace, SaveChanges])
    def set_updated_time(self):
        self.updated_at = datetime.datetime.now()

    class Settings:
        validate_on_save = True


class CompanyBase(BaseModel):
    username: EmailStr
    title: str
    public_email: EmailStr
    number_of_representatives: int
    additional_data: Optional[str]
class CompanyAndUserCreate(CompanyBase):
    username: EmailStr

class CompanyCreateResponse(CompanyBase):
    username: EmailStr
    id: int
    password: str

class CompanyUpdate(BaseModel):
    title: Optional[str]
    public_email: Optional[EmailStr]
    number_of_representatives: Optional[int]
    additional_data: Optional[str]

class CompanyUpdateResponse(CompanyBase):
    username: EmailStr
    id: int

class RefreshToken(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    is_revoked: bool = False