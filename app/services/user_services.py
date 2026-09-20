from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repository.user_repository import user_repository
from app.schemas.user import UserCreate, UserUpdate


def get_user(db:Session, user_id:int): 
    user=user_repository.get(db, user_id)
    if   not user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    return user

def list_users(db:Session):
    return user_repository.get_all(db)

def create_user(db:Session, data:UserCreate):
     if user_repository.get_by_username(db, data.username):
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
     return user_repository.create(db, data.model_dump())


def update_user(db:Session, user_id:int, data:UserUpdate):
    user=get_user(db, user_id)
    return user_repository.update(db, user, data.model_dump(exclude_unset=True))

def delete_user(db:Session, user_id:int):
    user=get_user(db, user_id)
    return user_repository.delete(db, user)