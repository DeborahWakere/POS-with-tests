from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql import func
from app.database import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    loyalty_points = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    receipt = relationship("Receipt", back_populates="customers")
    sales = relationship("Sale", back_populates="customers")