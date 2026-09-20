from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class InventoryBase(BaseModel):
    product_id: int
    quantity: int
    location: Optional[str] = None

class InventoryCreate(InventoryBase):
    pass

class InventoryUpdate(BaseModel):
    quantity: Optional[int] = None
    location: Optional[str] = None

class InventoryRead(InventoryBase):
    inventory_id: int
    updated_at: datetime | None = None
    model_config = ConfigDict(from_attributes=True)
