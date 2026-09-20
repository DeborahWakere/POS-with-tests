from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

class SupplierBase(BaseModel):
    supplier_name: str
    contact_person: str
    contact_number: str

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(SupplierBase):
    supplier_name: str | None = None
    contact_person: str | None = None
    contact_number: str | None = None


class SupplierRead(SupplierBase):
    model_config = ConfigDict(from_attributes=True)

    id:int = Field(validation_alias="supplier_id")
    created_at: datetime