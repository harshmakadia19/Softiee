from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    payment_type = Column(String(50)) # e.g., Credit Card, Cash
    card_last4 = Column(String(4))
    status = Column(String(50))       # pending / preparing / completed / failed
    amount = Column(DECIMAL(10, 2))
    paid_at = Column(DateTime)

    order = relationship("Order", back_populates="payment")