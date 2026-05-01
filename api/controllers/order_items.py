from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, Response, status

from ..models import order_item as model
from ..schemas import order_item as schema

def create(db: Session, request: schema.OrderItemCreate):
    try:
        new_order_item = model.OrderItem(
            order_id=request.order_id,
            menu_item_id=request.menu_item_id,
            quantity=request.quantity,
            unit_price=request.unit_price
        )
        db.add(new_order_item)
        db.commit()
        db.refresh(new_order_item)
        return new_order_item
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred while creating order item.")

def read_all_for_order(db: Session, order_id: int):
    return db.query(model.OrderItem).filter(model.OrderItem.order_id == order_id).all()

def delete(db: Session, item_id: int):
    order_item = db.query(model.OrderItem).filter(model.OrderItem.id == item_id).first()
    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")
    
    db.delete(order_item)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
