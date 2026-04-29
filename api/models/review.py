from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))
    rating = Column(Integer) # 1-5
    review_text = Column(Text)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    menu_item = relationship("MenuItem", back_populates="reviews")
    order = relationship("Order", back_populates="reviews")