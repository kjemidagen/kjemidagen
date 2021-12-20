from typing import TYPE_CHECKING, Optional
from sqlalchemy import func
from datetime import datetime
from sqlmodel import SQLModel, Relationship, Field
from pydantic import EmailStr

if TYPE_CHECKING:
    from kjemidagen.user import User

class CompanyBase(SQLModel):
    title: str
    email_address: EmailStr
    price: float
    additional_data: str
    created_at: Optional[datetime] = Field(sa_column_kwargs={"server_default": func.now()})
    updated_at: Optional[datetime] = Field(sa_column_kwargs={"server_default": func.now(), "server_onupdate": func.now()})


class Company(CompanyBase, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True, foreign_key="user.id")
    user: "User" = Relationship(back_populates="company")
