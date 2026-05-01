from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .order_item import OrderItem

class OrderBase(BaseModel):
    tracking_number: Optional[str] = None
    status: str
    order_type: str
    total_price: float

class OrderCreate(OrderBase):
    customer_id: int

class OrderUpdate(BaseModel):
    status: Optional[str] = None
    total_price: Optional[float] = None

class Order(OrderBase):
    id: int
    customer_id: int
    created_at: datetime
    order_items: List[OrderItem] = []

    class ConfigDict:
        from_attributes = True