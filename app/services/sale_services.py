from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repository.sale_repository import sale_repository
from app.schemas.sale import SaleCreate, SaleUpdate

def get_sale(db: Session, sale_id: int):
    sale = sale_repository.get(db, sale_id)
    if not sale: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sale with id {sale_id} not found")
    return sale

def list_sale(db: Session): return sale_repository.get_all(db)
def create_sale(db: Session, data: SaleCreate): return sale_repository.create(db, data.model_dump())
def update_sale(db: Session, sale_id: int, data: SaleUpdate):
    return sale_repository.update(db, get_sale(db, sale_id), data.model_dump(exclude_unset=True))
def delete_sale(db: Session, sale_id: int): return sale_repository.delete(db, get_sale(db, sale_id))
