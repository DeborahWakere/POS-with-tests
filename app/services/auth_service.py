from datetime import timedelta
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hashed_password,
    verify_password
)
from app.repository.user_repository import user_repository
from app.schemas.user import UserCreate

def register(db: Session, data: UserCreate):
    if user_repository.get_by_username(db, data.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken",
        )
    
    values = data.model_dump(exclude={"password"})
    values["password_hash"] = hashed_password(data.password)
    
    return user_repository.create(db, values)

def authentication(db: Session, username: str, password: str):
    user = user_repository.get_by_username(db, username)
    
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        payload: dict[str, Any] = decode_access_token(token)
        subject = payload.get("sub")
    except Exception:
        subject = None
    
    access_token_expires = timedelta(minutes=30) # Token valid for 30 minutes
    access_token = create_access_token(
        data={"sub": user.username}, 
        expires_delta=access_token_expires
    )
    
    return user
