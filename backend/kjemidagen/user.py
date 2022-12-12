import logging
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlmodel import Session, select

from kjemidagen.auth import get_current_user, get_current_admin
from kjemidagen.crypto import hash_password
from kjemidagen.database import get_session

from kjemidagen.models import (
    User,
    UserCreate,
    UserCreateResponse,
    UserGetResponse,
    UserUpdate,
    UserUpdateResponse,
)

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

user_router = APIRouter()


@user_router.get(
    "/", dependencies=[Depends(get_current_admin)], response_model=List[UserGetResponse]
)
async def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users")
    return [
        UserGetResponse(id=user.id, username=user.username, is_admin=user.is_admin)
        for user in users
    ]  # Yucky but nessecary because casting doesnt work


@user_router.get("/{user_id}", response_model=UserGetResponse)
async def get_user(
    user_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    if not (current_user.is_admin or current_user.id == user_id):
        raise credentials_exception
    user = session.exec(select(User).where(User.id == user_id)).one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="No users")
    return UserGetResponse(id=user.id, username=user.username, is_admin=user.is_admin)


@user_router.get("/self}", response_model=UserGetResponse)
async def get_user_self(user_id: int, current_user: User = Depends(get_current_user)):
    """Get info about current user"""
    if not (current_user.is_admin or current_user.id == user_id):
        raise credentials_exception
    return UserGetResponse(
        id=current_user.id,
        username=current_user.username,
        is_admin=current_user.is_admin,
    )


@user_router.post(
    "/", dependencies=[Depends(get_current_admin)], response_model=UserCreateResponse
)
async def create_user(user: UserCreate, session: Session = Depends(get_session)):
    check_if_taken = session.exec(
        select(User).where(User.username == user.username)
    ).all()

    if len(check_if_taken) > 0:
        raise HTTPException(status_code=409, detail="Username already taken")
    new_user = User(
        username=user.username, hashed_password=hash_password(password=user.password)
    )
    logging.info(f"Created users username is {user.username}")

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return UserCreateResponse(
        username=new_user.username, id=new_user.id, is_admin=new_user.is_admin
    )


@user_router.patch("/{user_id}", response_model=UserUpdateResponse)
async def edit_user(
    user_id: int,
    updated_user: UserUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    # todo: Egne exceptions for innlogget men ikke tilgang
    if not (current_user.is_admin or current_user.id == user_id):
        raise credentials_exception
    if updated_user.is_admin and not current_user.is_admin:
        raise credentials_exception

    user = session.exec(select(User).where(User.id == user_id)).one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    updated_data = updated_user.dict(
        exclude_unset=True
    )  # get only the values which are not empty
    if "password" in updated_data.keys():
        hashed_password = hash_password(updated_data.pop("password"))
        setattr(user, "hashed_password", hashed_password)
    for field, value in updated_data.items():
        setattr(user, field, value)

    session.add(user)
    session.commit()
    session.refresh(user)

    return UserCreateResponse(
        username=user.username, id=user.id, is_admin=user.is_admin
    )


@user_router.delete("/{user_id}", dependencies=[Depends(get_current_admin)])
async def delete_user(
    user_id: int,
    session: Session = Depends(get_session),
):
    user = session.exec(select(User).where(User.id == user_id)).one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    session.delete(user)
    session.commit()

    return {"ok": True}
