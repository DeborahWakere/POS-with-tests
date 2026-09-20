from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Numeric,
    DateTime,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class SaleItem(Base):
    __tablename__ = "saleitems"

    sale_item_id = Column(Integer, primary_key=True, index=True)
    quality = Column(Integer, nullable=False)
    unit_price = Column(Numeric, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    sale_id = Column(Integer, ForeignKey("sales.sale_id"), nullable=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True)

    sale = relationship("Sale", back_populates="sale_items")
    product = relationship("Product", back_populates="sale_items")