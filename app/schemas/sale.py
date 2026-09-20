from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

class SaleBase(BaseModel):
    sale_date: datetime
    total_amount: Decimal
    user_id: int | None = None
    customer_id: int | None = None

class SaleCreate(SaleBase):
    pass

class SaleUpdate(SaleBase):
    sale_date: datetime | None = None
    total_amount: Decimal | None = None
    user_id: int | None = None
    customer_id: int | None = None


class SaleRead(SaleBase):
    model_config = ConfigDict(from_attributes=True)

    id:int = Field(validation_alias="sale_id")
    created_at: datetime