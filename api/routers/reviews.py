from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from ..controllers import reviews as controller
from ..schemas import review as schema
from ..dependencies.database import get_db

router = APIRouter(tags=['Reviews'], prefix="/reviews")

@router.post("/", response_model=schema.Review)
def create(request: schema.ReviewCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Review])
def read_all(menu_item_id: int = Query(None), db: Session = Depends(get_db)):
    return controller.read_all(db, menu_item_id)

@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(review_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, review_id)

from ..models import review as model
@router.get("/dish/{menu_item_id}", response_model=list[schema.Review])
def read_reviews_per_dish(menu_item_id: int, db: Session = Depends(get_db)):
    return db.query(model.Review).filter(model.Review.menu_item_id == menu_item_id).all()
