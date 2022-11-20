import datetime
import re
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel, EmailStr
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


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # type: ignore
    username: str = Field(index=True)  # type: ignore
    hashed_password: str
    is_admin: bool = False
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    company: Optional["Company"] = Relationship(back_populates="user")


class UserCreate(CamelBaseModel):
    username: EmailStr
    password: str


class UserCreateResponse(CamelBaseModel):
    """Contains fields returned on user creation"""

    username: EmailStr
    id: int
    is_admin: bool


class UserGetResponse(CamelBaseModel):
    """Contains fields returned from get requests"""

    username: EmailStr
    id: int
    is_admin: bool


class UserUpdate(CamelBaseModel):
    """Contains fields which you can update"""

    username: Optional[EmailStr]
    is_admin: Optional[bool]
    password: Optional[str]


class UserUpdateResponse(CamelBaseModel):
    username: EmailStr
    id: int
    is_admin: bool


class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # type: ignore
    user_id: int = Field(default=None, index=True, foreign_key="user.id")
    user: User = Relationship(back_populates="company")
    title: str = Field(index=True)  # type: ignore
    public_email: EmailStr
    number_of_representatives: Optional[int]
    additional_data: Optional[str]
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)


class CompanyAndUserCreate(CamelBaseModel):
    username: EmailStr
    title: str
    number_of_representatives: Optional[int] = 0
    public_email: EmailStr
    additional_data: Optional[str]


class CompanyCreateResponse(CamelBaseModel):
    username: EmailStr
    id: int
    password: str


class CompanyUpdate(CamelBaseModel):
    title: Optional[str]
    public_email: Optional[EmailStr]
    number_of_representatives: Optional[int]
    additional_data: Optional[str]


class CompanyUpdateResponse(CamelBaseModel):
    username: EmailStr
    id: int


class RefreshToken(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)  # type: ignore
    is_revoked: bool = False


class TokenResponse(CamelBaseModel):
    email: EmailStr
    access_token: str
    access_token_exp: int
    token_type: str = "bearer"
