from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import order_items as controller
from ..schemas import order_item as schema
from ..dependencies.database import get_db

router = APIRouter(tags=['Order Details'], prefix="/order-items")

@router.post("/", response_model=schema.OrderItem)
def create(request: schema.OrderItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/order/{order_id}", response_model=list[schema.OrderItem])
def read_by_order(order_id: int, db: Session = Depends(get_db)):
    return controller.read_all_for_order(db, order_id)
