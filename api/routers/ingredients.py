from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from typing import List

from ..controllers import ingredients as controller
from ..schemas import ingredient as schema
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/ingredients",
    tags=['Ingredients']
)

@router.post("/", response_model=schema.IngredientResponse, status_code=status.HTTP_201_CREATED)
def create(request: schema.IngredientCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=List[schema.IngredientResponse])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{ingredient_id}", response_model=schema.IngredientResponse)
def read_one(ingredient_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, ingredient_id)

@router.put("/{ingredient_id}", response_model=schema.IngredientResponse)
def update(ingredient_id: int, request: schema.IngredientUpdate, db: Session = Depends(get_db)):
    return controller.update(db, ingredient_id, request)

@router.delete("/{ingredient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(ingredient_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, ingredient_id)
