from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True)
    phone = Column(String(20))
    address = Column(Text)

    orders = relationship("Order", back_populates="customer")