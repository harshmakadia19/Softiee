from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import item_ingredients as controller
from ..schemas import item_ingredient as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Item Ingredients'],
    prefix="/item-ingredients"
)

@router.post("/", response_model=schema.ItemIngredient)
def create(request: schema.ItemIngredientCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.ItemIngredient])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.ItemIngredient)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.ItemIngredient)
def update(item_id: int, request: schema.ItemIngredientUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)