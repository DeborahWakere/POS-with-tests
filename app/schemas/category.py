from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: str | None = None

class CategoryRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(validation_alias="category_id")
    name: str = Field(validation_alias="category_name")
    created_at: datetime | None = None
