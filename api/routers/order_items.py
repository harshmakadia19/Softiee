from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from typing import List

from ..controllers import order_items as controller
from ..schemas import order_item as schema
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/order-items",
    tags=['Order Items']
)

@router.post("/", response_model=schema.OrderItemResponse, status_code=status.HTTP_201_CREATED)
def create(request: schema.OrderItemCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/order/{order_id}", response_model=List[schema.OrderItemResponse])
def read_all_for_order(order_id: int, db: Session = Depends(get_db)):
    return controller.read_all_for_order(db, order_id)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)
