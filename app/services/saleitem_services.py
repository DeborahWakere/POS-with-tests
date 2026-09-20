from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repository.saleitem_repository import saleitem_repository
from app.schemas.saleitem import SaleItemCreate, SaleItemUpdate

def get_saleitem(db: Session, sale_item_id: int):
    obj = saleitem_repository.get(db, sale_item_id)
    if not obj: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sale item with id {sale_item_id} not found")
    return obj

def list_saleitems(db: Session): return saleitem_repository.get_all(db)
def create_saleitem(db: Session, data: SaleItemCreate): return saleitem_repository.create(db, data.model_dump())
def update_saleitem(db: Session, sale_item_id: int, data: SaleItemUpdate):
    return saleitem_repository.update(db, get_saleitem(db, sale_item_id), data.model_dump(exclude_unset=True))
def delete_saleitem(db: Session, sale_item_id: int): return saleitem_repository.delete(db, get_saleitem(db, sale_item_id))
