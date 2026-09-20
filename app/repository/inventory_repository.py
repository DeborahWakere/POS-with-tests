from sqlalchemy.orm import Session
from app.models.inventory import Inventory

class InventoryRepository:
    def get_by_id(self, db: Session, inventory_id: int):
        return db.get(Inventory, inventory_id)

    def get_by_product(self, db: Session, product_id: int):
        return db.query(Inventory).filter(Inventory.product_id == product_id).first()

    def get_all(self, db: Session):
        return db.query(Inventory).all()

    def create(self, db: Session, data: dict):
        inventory = Inventory(**data)
        db.add(inventory)
        db.commit()
        db.refresh(inventory)
        return inventory

    def update(self, db: Session, db_obj: Inventory, data: dict):
        for field, value in data.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: Inventory):
        db.delete(db_obj)
        db.commit()

inventory_repository = InventoryRepository()
