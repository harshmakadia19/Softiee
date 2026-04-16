from typing import Optional
from pydantic import BaseModel

class OrderPromoBase(BaseModel):
    order_id: int
    promo_id: int

class OrderPromoCreate(OrderPromoBase):
    pass

class OrderPromoUpdate(BaseModel):
    order_id: Optional[int] = None
    promo_id: Optional[int] = None

class OrderPromo(OrderPromoBase):
    id: int

    class ConfigDict:
        from_attributes = True