from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    ForeignKey, 
    DateTime
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Inventory(Base):
    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), unique=True, nullable=False)
    quantity = Column(Integer, default=0, nullable=False)
    location = Column(String(100), nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    product = relationship("Product", back_populates="inventory")
