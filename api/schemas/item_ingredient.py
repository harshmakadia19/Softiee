from typing import Optional
from pydantic import BaseModel

class ItemIngredientBase(BaseModel):
    quantity_required: float

class ItemIngredientCreate(ItemIngredientBase):
    menu_item_id: int
    ingredient_id: int

class ItemIngredientUpdate(BaseModel):
    menu_item_id: Optional[int] = None
    ingredient_id: Optional[int] = None
    quantity_required: Optional[float] = None

class ItemIngredient(ItemIngredientBase):
    id: int
    menu_item_id: int
    ingredient_id: int

    class ConfigDict:
        from_attributes = True