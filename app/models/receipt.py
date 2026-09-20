from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Receipt(Base):
    __tablename__ = "receipts"

    receipt_id = Column(Integer, primary_key=True, index=True)
    receipt_barcode = Column(Integer, unique=True, nullable=False)
    issued_at = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True, nullable=False)

    sale_id = Column(Integer, ForeignKey("sales.sale_id"), nullable=True)
    payment_id = Column(Integer, ForeignKey("payments.payment_id"), nullable=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=True)

    sale = relationship("Sale", back_populates="receipts")
    payments = relationship("Payment", back_populates="receipt")
    customers = relationship("Customer", back_populates="receipt")