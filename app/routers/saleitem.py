from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.saleitem import SaleItemCreate, SaleItemRead, SaleItemUpdate
from app.services import saleitem_services


router = APIRouter(prefix="/saleitems", tags=["saleitems"])


@router.get("/", response_model=list[SaleItemRead])
def list_saleitems(db: Session = Depends(get_db)):
    return saleitem_services.list_saleitems(db)


@router.get("/{saleitem_id}", response_model=SaleItemRead)
def get_saleitem(saleitem_id: int, db: Session = Depends(get_db)):
    return saleitem_services.get_saleitem(db, saleitem_id)


@router.post("/", response_model=SaleItemRead, status_code=status.HTTP_201_CREATED)
def create_saleitem(data: SaleItemCreate, db: Session = Depends(get_db)):
    return saleitem_services.create_saleitem(db, data)


@router.put("/{saleitem_id}", response_model=SaleItemRead)
def update_saleitem(
    saleitem_id: int,
    data: SaleItemUpdate,
    db: Session = Depends(get_db)
):
    return saleitem_services.update_saleitem(db, saleitem_id, data)


@router.delete("/{saleitem_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_saleitem(saleitem_id: int, db: Session = Depends(get_db)):
    saleitem_services.delete_saleitem(db, saleitem_id)
    return None