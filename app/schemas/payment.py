from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

class PaymentBase(BaseModel):
    payment_method: str
    amount_paid: Decimal
    sale_id: int | None = None

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(PaymentBase):
    payment_method: str | None = None
    amount_paid: Decimal| None = None
    sale_id: int | None = None



class PaymentRead(PaymentBase):
    model_config = ConfigDict(from_attributes=True)

    id:int = Field(validation_alias="payment_id")
    created_at: datetime