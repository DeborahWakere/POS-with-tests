from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.services import user_services

router= APIRouter( prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserRead])
def  listusers(db:Session = Depends(get_db)): 
    return user_services.list_users(db)
            
@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id:int, db:Session = Depends(get_db)): 
    return user_services.get_user(db, user_id)

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(data:UserCreate, db:Session = Depends(get_db)): 
    return user_services.create_user(db, data)

@router.put("/{user_id}", response_model=UserRead)
def update_user(
    user_id:int, data:UserUpdate, db:Session = Depends(get_db)): 
    return user_services.update_user(db, user_id, data)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id:int, db:Session = Depends(get_db)):
    return user_services.delete_user(db, user_id)