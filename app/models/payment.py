from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    Numeric,
    DateTime,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True, nullable=False)
    payment_method = Column(String, nullable=False)
    amount_paid = Column(Numeric, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    sale_id = Column(Integer, ForeignKey("sales.sale_id"), nullable=True)

    sale = relationship("Sale", back_populates="payments")
    receipt = relationship("Receipt", back_populates="payments")