from sqlalchemy.orm import Session

from app.models.sale import Sale


class SaleRepository:

    def get(self, db: Session, sale_id: int):
        return db.get(Sale, sale_id)

    def get_all(self, db: Session):
        return db.query(Sale).all()

    def get_by_user(self, db: Session, user_id: int):
        return db.query(Sale).filter(
            Sale.user_id == user_id
        ).all()

    def get_by_customer(self, db: Session, customer_id: int):
        return db.query(Sale).filter(
            Sale.customer_id == customer_id
        ).all()

    def create(self, db: Session, data: dict):
        sale = Sale(**data)

        db.add(sale)
        db.commit()
        db.refresh(sale)

        return sale

    def update(self, db: Session, db_obj: Sale, data: dict):
        for field, value in data.items():
            setattr(db_obj, field, value)

        db.commit()
        db.refresh(db_obj)

        return db_obj

    def delete(self, db: Session, db_obj: Sale):
        db.delete(db_obj)
        db.commit()

        return db_obj


sale_repository = SaleRepository()