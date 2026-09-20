from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repository.category_repository import category_repository
from app.schemas.category import CategoryCreate, CategoryUpdate

def get_category(db: Session, category_id: int):
    category = category_repository.get(db, category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {category_id} not found")
    return category

def list_categories(db: Session): return category_repository.get_all(db)
def create_category(db: Session, data: CategoryCreate):
    return category_repository.create(db, {"category_name": data.name})
def update_category(db: Session, category_id: int, data: CategoryUpdate):
    values = data.model_dump(exclude_unset=True)
    if "name" in values: values["category_name"] = values.pop("name")
    return category_repository.update(db, get_category(db, category_id), values)
def delete_category(db: Session, category_id: int): return category_repository.delete(db, get_category(db, category_id))
