from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    payment_type: str
    card_last4: Optional[str] = None
    status: str
    amount: float

class PaymentCreate(PaymentBase):
    order_id: int

class PaymentUpdate(BaseModel):
    status: Optional[str] = None

class Payment(PaymentBase):
    id: int
    order_id: int
    paid_at: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True