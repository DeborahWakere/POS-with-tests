from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repository.receipt_repository import receipt_repository
from app.schemas.receipt import ReceiptCreate, ReceiptUpdate


def get_receipt(db: Session, receipt_id: int):
    receipt = receipt_repository.get(db, receipt_id)

    if not receipt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Receipt with id {receipt_id} not found"
        )

    return receipt


def list_receipts(db: Session):
    return receipt_repository.get_all(db)


def create_receipt(db: Session, data: ReceiptCreate):
    existing = receipt_repository.get_all(db)
    if any(r.receipt_barcode == data.receipt_barcode for r in existing):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Receipt barcode already exists")
    return receipt_repository.create(db, data.model_dump())


def update_receipt(db: Session, receipt_id: int, data: ReceiptUpdate):
    receipt = get_receipt(db, receipt_id)

    return receipt_repository.update(
        db,
        receipt,
        data.model_dump(exclude_unset=True)
    )


def delete_receipt(db: Session, receipt_id: int):
    receipt = get_receipt(db, receipt_id)

    return receipt_repository.delete(db, receipt)