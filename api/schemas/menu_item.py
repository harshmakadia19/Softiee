from typing import Optional
from pydantic import BaseModel

class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    calories: Optional[int] = None
    category: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    category: Optional[str] = None
    available: Optional[bool] = None

class MenuItem(MenuItemBase):
    id: int
    available: bool

    class ConfigDict:
        from_attributes = True