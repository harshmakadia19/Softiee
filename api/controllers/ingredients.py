from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, Response, status

from ..models import ingredient as model
from ..schemas import ingredient as schema

def create(db: Session, request: schema.IngredientCreate):
    try:
        new_ingredient = model.Ingredient(
            name=request.name,
            amount=request.amount,
            unit=request.unit
        )
        db.add(new_ingredient)
        db.commit()
        db.refresh(new_ingredient)
        return new_ingredient
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred while creating ingredient.")

def read_all(db: Session):
    return db.query(model.Ingredient).all()

def read_one(db: Session, ingredient_id: int):
    ingredient = db.query(model.Ingredient).filter(model.Ingredient.id == ingredient_id).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient

def update(db: Session, ingredient_id: int, request: schema.IngredientUpdate):
    ingredient = read_one(db, ingredient_id)
    
    update_data = request.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(ingredient, key, value)
        
    db.commit()
    db.refresh(ingredient)
    return ingredient

def delete(db: Session, ingredient_id: int):
    ingredient = read_one(db, ingredient_id)
    db.delete(ingredient)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
