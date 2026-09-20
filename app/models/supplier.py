from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from app.models.product import Product

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(Integer, primary_key=True, index=True)
    supplier_name = Column(String, unique=True,index=True, nullable=False)
    contact_person = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    products = relationship("Product", back_populates="supplier")