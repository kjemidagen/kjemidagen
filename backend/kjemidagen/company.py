from typing import TYPE_CHECKING, Optional, List
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy import func
from datetime import datetime
from sqlalchemy.sql.expression import update
from sqlmodel import SQLModel, Relationship, Field, select
from pydantic import EmailStr
from sqlmodel.ext.asyncio.session import AsyncSession
from kjemidagen.auth import get_current_admin, get_current_user
from kjemidagen.crypto import generate_random_password, hash_password

from kjemidagen.database import get_session
from kjemidagen.user import User, UserBase, UserCreate, UserCreateResponse

class CompanyBase(SQLModel):
    title: str
    email_address: EmailStr
    number_of_representatives: int
    additional_data: Optional[str]
    created_at: Optional[datetime] = Field(sa_column_kwargs={"server_default": func.now()})
    updated_at: Optional[datetime] = Field(sa_column_kwargs={"server_default": func.now(), "server_onupdate": func.now()})

class Company(CompanyBase, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True, foreign_key="user.id")
    user: "User" = Relationship(back_populates="company")

class CompanyAndUserCreate(CompanyBase, UserBase):
    pass
class CompanyCreateResponse(CompanyBase, UserBase):
    password: str
class CompanyEditResponse(CompanyBase, UserBase):
    pass
class CompanyUpdate(SQLModel):
    title: Optional[str]
    email_address: Optional[EmailStr]
    number_of_representatives: Optional[int]
    additional_data: Optional[int]
    password: Optional[str]

credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
)

company_router = APIRouter()

@company_router.get("/", dependencies=[Depends(get_current_admin)])
async def get_companies(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Company))
    companies: List[Company] = result.all()
    if not companies:
        raise credentials_exception
    return companies

@company_router.get("/{company_id}")
async def get_company(company_id, current_user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    if not ( current_user.is_admin or current_user.id == company_id ):
        raise credentials_exception
    company = await session.get(Company, company_id)
    if not company:
        raise HTTPException(status_code=404, detail=f"No company with id {company_id}")
    return company

@company_router.post("/", dependencies=[Depends(get_current_admin)], response_model=CompanyCreateResponse)
async def create_company(company: CompanyAndUserCreate, session: AsyncSession = Depends(get_session)):
    generated_password = generate_random_password()
    user = User(
        username=company.username,
        hashed_password=hash_password(generated_password))
    company_in_db = Company(
        title=company.title,
        email_address=company.email_address,
        number_of_representatives=company.number_of_representatives,
        additional_data=company.additional_data,
        user = user
    )
    session.add(user)
    session.add(company_in_db)
    await session.commit()
    await session.refresh(user)
    await session.refresh(company_in_db)

    return CompanyCreateResponse(
        username=company_in_db.user.username,
        id=company_in_db.user_id,
        is_admin=company_in_db.user.is_admin,
        title=company_in_db.title,
        email_address=company_in_db.email_address,
        number_of_representatives=company_in_db.number_of_representatives,
        additional_data=company_in_db.additional_data,
        password=generated_password,
        created_at=company_in_db.created_at,
        updated_at=company_in_db.updated_at
    )

@company_router.patch("/{company_id}")
async def edit_company(company_id: int, updated_company: CompanyUpdate, session: AsyncSession = Depends(get_session)):
    company = await session.get(Company, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="User not found")
    updated_data = updated_company.dict(exclude_unset=True) # get only the values which are not empty
    if "password" in updated_data.keys:
        updated_data["hashed_password"] = hash_password(updated_data["password"])
        updated_data.pop("password")

    for field, value in updated_data.items():
        setattr(company, field, value)
    session.add(company)
    await session.commit()
    await session.refresh(company)
    return CompanyCreateResponse.from_orm(company)
