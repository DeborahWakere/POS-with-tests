from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

class SaleItemBase(BaseModel):
    quality: int
    unit_price: Decimal
    sale_id: int | None = None
    product_id: int | None = None

class SaleItemCreate(SaleItemBase):
    pass

class SaleItemUpdate(SaleItemBase):
    quality: int | None = None
    unit_price: Decimal | None = None
    sale_id: int | None = None
    product_id: int | None = None


class SaleItemRead(SaleItemBase):
    model_config = ConfigDict(from_attributes=True)

    id:int = Field(validation_alias="sale_item_id")
    created_at: datetime