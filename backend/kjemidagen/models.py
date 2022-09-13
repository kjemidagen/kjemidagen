import datetime
import uuid
import pymongo
import re
from beanie import Document, Indexed, Link, Insert, Replace, SaveChanges, before_event
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


def to_camel(string: str):
    """snake_case to camelCase"""

    def camel(match: re.Match):
        return match.group(1) + match.group(2).upper()

    return re.sub(r"(.*?)_([a-z])", camel, string)


class CamelBaseModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class User(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)  # type: ignore
    username: Indexed(str, index_type=pymongo.TEXT, unique=True)  # type: ignore
    hashed_password: str
    is_admin: bool = False
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    @before_event([Replace, SaveChanges])
    def set_updated_time(self):
        self.updated_at = datetime.datetime.now()

    class Settings:
        validate_on_save = True


class UserCreate(CamelBaseModel):
    username: EmailStr
    password: str


class UserCreateResponse(CamelBaseModel):
    """Contains fields returned on user creation"""

    username: EmailStr
    id: uuid.UUID
    is_admin: bool


class UserGetResponse(CamelBaseModel):
    """Contains fields returned from get requests"""

    username: EmailStr
    id: uuid.UUID
    is_admin: bool


class UserUpdate(CamelBaseModel):
    """Contains fields which you can update"""

    username: Optional[EmailStr]
    is_admin: Optional[bool]
    password: Optional[str]


class UserUpdateResponse(CamelBaseModel):
    username: EmailStr
    id: uuid.UUID
    is_admin: bool


class Company(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)  # type: ignore
    user: Link[User]
    title: Indexed(str)  # type: ignore
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


class CompanyBase(CamelBaseModel):
    username: EmailStr
    title: str
    public_email: EmailStr
    number_of_representatives: int
    additional_data: Optional[str]


class CompanyAndUserCreate(CompanyBase):
    username: EmailStr


class CompanyCreateResponse(CompanyBase):
    username: EmailStr
    id: uuid.UUID
    password: str


class CompanyUpdate(CamelBaseModel):
    title: Optional[str]
    public_email: Optional[EmailStr]
    number_of_representatives: Optional[int]
    additional_data: Optional[str]


class CompanyUpdateResponse(CompanyBase):
    username: EmailStr
    id: uuid.UUID


class RefreshToken(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)  # type: ignore
    is_revoked: bool = False


class TokenResponse(CamelBaseModel):
    email: EmailStr
    access_token: str
    access_token_exp: int
    token_type: str = "bearer"
