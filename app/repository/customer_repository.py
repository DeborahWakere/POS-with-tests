from sqlalchemy.orm import Session
from app.models.customer import Customer

class CustomerRepository:
    def get(self, db: Session, customer_id: int):
        return db.get(Customer, customer_id)
    def get_all(self, db: Session):
        return db.query(Customer).all()
    def create(self, db: Session, data: dict):
        customer = Customer(**data)
        db.add(customer); db.commit(); db.refresh(customer)
        return customer
    def update(self, db: Session, db_obj: Customer, data: dict):
        for field, value in data.items(): setattr(db_obj, field, value)
        db.commit(); db.refresh(db_obj)
        return db_obj
    def delete(self, db: Session, db_obj: Customer):
        db.delete(db_obj); db.commit(); return db_obj
customer_repository = CustomerRepository()
