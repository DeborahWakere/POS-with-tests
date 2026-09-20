from sqlalchemy.orm import Session

from app.models.receipt import Receipt


class ReceiptRepository:

    def get(self, db: Session, receipt_id: int):
        return db.get(Receipt, receipt_id)

    def get_all(self, db: Session):
        return db.query(Receipt).all()

    def get_by_sale(self, db: Session, sale_id: int):
        return db.query(Receipt).filter(
            Receipt.sale_id == sale_id
        ).all()

    def get_by_payment(self, db: Session, payment_id: int):
        return db.query(Receipt).filter(
            Receipt.payment_id == payment_id
        ).all()

    def get_by_customer(self, db: Session, customer_id: int):
        return db.query(Receipt).filter(
            Receipt.customer_id == customer_id
        ).all()

    def create(self, db: Session, data: dict):
        receipt = Receipt(**data)

        db.add(receipt)
        db.commit()
        db.refresh(receipt)

        return receipt

    def update(self, db: Session, db_obj: Receipt, data: dict):
        for field, value in data.items():
            setattr(db_obj, field, value)

        db.commit()
        db.refresh(db_obj)

        return db_obj

    def delete(self, db: Session, db_obj: Receipt):
        db.delete(db_obj)
        db.commit()

        return db_obj


receipt_repository = ReceiptRepository()