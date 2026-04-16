from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
import enum

class OrderStatus(str, enum.Enum):
    PENDING = "pending"
    PREPARING = "preparing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class OrderType(str, enum.Enum):
    TAKEOUT = "takeout"
    DELIVERY = "delivery"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    tracking_number = Column(String(36), unique=True)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)
    order_type = Column(String(20)) # Takeout/Delivery
    total_price = Column(DECIMAL(10, 2))
    created_at = Column(DATETIME, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")
    payment = relationship("Payment", back_populates="order", uselist=False)
    promos = relationship("OrderPromo", back_populates="order")