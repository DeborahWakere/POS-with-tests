from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    loyalty_points: int

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None
    loyalty_points: int| None = None


class CustomerRead(CustomerBase):
    model_config = ConfigDict(from_attributes=True)

    id:int = Field(validation_alias="customer_id")
    created_at: datetime