from sqlalchemy import Column, Integer, String, Text, DECIMAL, Boolean
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(8, 2))
    calories = Column(Integer)
    category = Column(String(60))
    available = Column(Boolean, default=True)

    ingredients = relationship("ItemIngredient", back_populates="menu_item")
    order_items = relationship("OrderItem", back_populates="menu_item")
    reviews = relationship("Review", back_populates="menu_item")