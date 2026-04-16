from typing import Optional
from pydantic import BaseModel

class IngredientBase(BaseModel):
    name: str
    amount: float
    unit: str

class IngredientCreate(IngredientBase):
    pass

class IngredientUpdate(BaseModel):
    name: Optional[str] = None
    amount: Optional[float] = None
    unit: Optional[str] = None

class Ingredient(IngredientBase):
    id: int

    class ConfigDict:
        from_attributes = True