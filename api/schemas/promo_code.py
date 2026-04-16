from datetime import date
from typing import Optional
from pydantic import BaseModel

class PromoCodeBase(BaseModel):
    code: str
    discount_pct: float
    expiration_date: date

class PromoCodeCreate(PromoCodeBase):
    pass

class PromoCodeUpdate(BaseModel):
    code: Optional[str] = None
    discount_pct: Optional[float] = None
    expiration_date: Optional[date] = None
    active: Optional[bool] = None

class PromoCode(PromoCodeBase):
    id: int
    active: bool

    class ConfigDict:
        from_attributes = True