from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

class ReceiptBase(BaseModel):
    receipt_barcode: int
    issued_at: datetime
    sale_id: int | None = None
    payment_id: int | None = None
    customer_id: int | None = None
    is_active: bool = True

class ReceiptCreate(ReceiptBase):
    pass

class ReceiptUpdate(ReceiptBase):
    receipt_barcode: int | None = None
    issued_at: datetime | None = None
    sale_id: int | None = None
    payment_id: int | None = None
    customer_id: int | None = None


class ReceiptRead(  ReceiptBase):
    model_config = ConfigDict(from_attributes=True)

    id:int = Field(validation_alias="receipt_id")
    created_at: datetime