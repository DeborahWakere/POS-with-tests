from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class UserBase(BaseModel):
    username: str
    password_hash: str
    user_role: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    username: str | None = None
    password_hash: str | None = None
    user_role: str | None = None


class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id:int = Field(validation_alias="user_id")
    is_active: bool
    created_at: datetime