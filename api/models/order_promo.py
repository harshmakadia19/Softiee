from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class OrderPromo(Base):
    __tablename__ = "order_promo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    promo_id = Column(Integer, ForeignKey("promo_codes.id"))

    order = relationship("Order", back_populates="promos")
    promo = relationship("PromoCode", back_populates="orders")