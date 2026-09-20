from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.inventory import InventoryRead, InventoryCreate, InventoryUpdate
from app.services.inventory_services import inventory_service


router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.get("/", response_model=List[InventoryRead])
def read_all_inventory(db: Session = Depends(get_db)):
    return inventory_service.get_all_inventory(db)


@router.get("/{inventory_id}", response_model=InventoryRead)
def read_inventory(inventory_id: int, db: Session = Depends(get_db)):
    return inventory_service.get_inventory(db, inventory_id)


@router.post("/", response_model=InventoryRead, status_code=status.HTTP_201_CREATED)
def create_inventory(payload: InventoryCreate, db: Session = Depends(get_db)):
    return inventory_service.create_inventory(db, payload)


@router.patch("/{inventory_id}", response_model=InventoryRead)
def update_inventory(
    inventory_id: int,
    payload: InventoryUpdate,
    db: Session = Depends(get_db)
):
    return inventory_service.update_inventory(db, inventory_id, payload)


@router.delete("/{inventory_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inventory(inventory_id: int, db: Session = Depends(get_db)):
    inventory_service.delete_inventory(db, inventory_id)
    return None