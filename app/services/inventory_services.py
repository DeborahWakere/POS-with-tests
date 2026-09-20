from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repository.inventory_repository import inventory_repository
from app.schemas.inventory import InventoryCreate, InventoryUpdate


class InventoryService:
    def get_inventory(self, db: Session, inventory_id: int):
        inventory = inventory_repository.get_by_id(db, inventory_id)
        if not inventory:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Inventory record not found"
            )
        return inventory

    def get_all_inventory(self, db: Session):
        return inventory_repository.get_all(db)

    def create_inventory(self, db: Session, schema_data: InventoryCreate):
        existing = inventory_repository.get_by_product(db, schema_data.product_id)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Inventory for this product already exists"
            )
        return inventory_repository.create(db, schema_data.model_dump())

    def update_inventory(self, db: Session, inventory_id: int, schema_data: InventoryUpdate):
        inventory = self.get_inventory(db, inventory_id)
        update_data = schema_data.model_dump(exclude_unset=True)
        return inventory_repository.update(db, inventory, update_data)

    def delete_inventory(self, db: Session, inventory_id: int):
        inventory = self.get_inventory(db, inventory_id)
        inventory_repository.delete(db, inventory)
        return {"detail": "Inventory record successfully deleted"}


inventory_service = InventoryService()