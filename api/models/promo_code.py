from sqlalchemy import Column, Integer, String, Float, Date, Boolean
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class PromoCode(Base):
    __tablename__ = "promo_codes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(30), unique=True)
    discount_pct = Column(Float)
    expiration_date = Column(Date)
    active = Column(Boolean, default=True)

    orders = relationship("OrderPromo", back_populates="promo")