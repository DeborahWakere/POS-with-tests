from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.receipt import ReceiptCreate, ReceiptRead, ReceiptUpdate
from app.services import receipt_services


router = APIRouter(prefix="/receipts", tags=["receipts"])


@router.get("/", response_model=list[ReceiptRead])
def list_receipts(db: Session = Depends(get_db)):
    return receipt_services.list_receipts(db)


@router.get("/{receipt_id}", response_model=ReceiptRead)
def get_receipt(receipt_id: int, db: Session = Depends(get_db)):
    return receipt_services.get_receipt(db, receipt_id)


@router.post("/", response_model=ReceiptRead, status_code=status.HTTP_201_CREATED)
def create_receipt(data: ReceiptCreate, db: Session = Depends(get_db)):
    return receipt_services.create_receipt(db, data)


@router.put("/{receipt_id}", response_model=ReceiptRead)
def update_receipt(
    receipt_id: int,
    data: ReceiptUpdate,
    db: Session = Depends(get_db)
):
    return receipt_services.update_receipt(db, receipt_id, data)


@router.delete("/{receipt_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_receipt(receipt_id: int, db: Session = Depends(get_db)):
    receipt_services.delete_receipt(db, receipt_id)
    return None