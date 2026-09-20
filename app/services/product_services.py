from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repository.category_repository import category_repository
from app.repository.supplier_repository import supplier_repository
from app.repository.product_repository import product_repository
from app.schemas.product import ProductCreate, ProductUpdate


def get_product(db:Session, id:int): 
    product=product_repository.get(db, id)
    if   not product:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not found"
        )
    return product

def list_products(db:Session):
    return product_repository.get_all(db)

def create_product(db: Session, data: ProductCreate):

    if product_repository.get_all(db) and any(p.sku == data.sku for p in product_repository.get_all(db)):
        raise HTTPException(status_code=400, detail="SKU already exists")

    category = category_repository.get(db, data.category_id)

    if not category:
        raise HTTPException(
            status_code=404,
            detail=f"Category {data.category_id} not found"
        )

    supplier = supplier_repository.get(db, data.supplier_id)

    if not supplier:
        raise HTTPException(
            status_code=404,
            detail=f"Supplier {data.supplier_id} not found"
        )

    return product_repository.create(db, data.model_dump())

def update_product(db:Session, product_id:int, data:ProductUpdate): 
    product=get_product(db, product_id)
    return product_repository.update(db, product, data.model_dump(exclude_unset=True))

def delete_product(db:Session, product):
    return product_repository.delete(db, product)