from sqlalchemy.orm import Session
from app.models.payment import Payment

class PaymentRepository:
    def get(self, db: Session, payment_id: int): return db.get(Payment, payment_id)
    def get_all(self, db: Session): return db.query(Payment).all()
    def get_by_sale(self, db: Session, sale_id: int): return db.query(Payment).filter(Payment.sale_id == sale_id).all()
    def create(self, db: Session, data: dict):
        payment = Payment(**data); db.add(payment); db.commit(); db.refresh(payment); return payment
    def update(self, db: Session, db_obj: Payment, data: dict):
        for field, value in data.items(): setattr(db_obj, field, value)
        db.commit(); db.refresh(db_obj); return db_obj
    def delete(self, db: Session, db_obj: Payment): db.delete(db_obj); db.commit(); return db_obj
payment_repository = PaymentRepository()
