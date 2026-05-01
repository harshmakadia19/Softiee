from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import order_promo as controller
from ..schemas import order_promo as schema
from ..dependencies.database import get_db

router = APIRouter(tags=['Order Promos'], prefix="/order-promos")

@router.post("/", response_model=schema.OrderPromo)
def create(request: schema.OrderPromoCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.OrderPromo])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.put("/{item_id}", response_model=schema.OrderPromo)
def update(item_id: int, request: schema.OrderPromoUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)