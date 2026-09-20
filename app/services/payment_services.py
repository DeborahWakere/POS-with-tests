from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repository.payment_repository import payment_repository
from app.schemas.payment import PaymentCreate, PaymentUpdate


def get_payment(db:Session, payment_id:int): 
    payment=payment_repository.get(db, payment_id)
    if   not payment:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND, detail=f"Payment with id {payment_id} not found"
        )
    return payment

def list_payment(db:Session):
    return payment_repository.get_all(db)

def create_payment(db:Session, data:PaymentCreate):
     return payment_repository.create(db, data.model_dump())


def update_payment(db:Session, payment_id:int, data:PaymentUpdate):
    payment=get_payment(db, payment_id)
    return payment_repository.update(db, payment, data.model_dump(exclude_unset=True))

def delete_payment(db:Session, payment_id:int): 
    payment=get_payment(db, payment_id)
    return payment_repository.delete(db, payment)