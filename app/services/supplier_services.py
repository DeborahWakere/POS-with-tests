from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repository.supplier_repository import supplier_repository
from app.schemas.supplier import SupplierCreate, SupplierUpdate


def get_supplier(db:Session, supplier_id:int):
    supplier=supplier_repository.get(db, supplier_id)
    if   not supplier:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND, detail=f"Supplier with id {id} not found"
        )
    return supplier

def list_suppliers(db:Session):
    return supplier_repository.get_all(db)

def create_supplier(db:Session, data:SupplierCreate):
     if any(s.supplier_name == data.supplier_name for s in supplier_repository.get_all(db)):
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Supplier already exists")
     return supplier_repository.create(db, data.model_dump())


def update_supplier(db:Session, supplier_id:int, data:SupplierUpdate): 
    supplier=get_supplier(db, supplier_id)
    return supplier_repository.update(db, supplier, data.model_dump(exclude_unset=True))

def delete_supplier(db:Session, supplier_id:int): 
    supplier=get_supplier(db, supplier_id)
    return supplier_repository.delete(db, supplier)