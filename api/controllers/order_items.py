from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import order_item as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_item = model.OrderItem(
        order_id=request.order_id,
        menu_item_id=request.menu_item_id,
        quantity=request.quantity,
        unit_price=request.unit_price
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_item

def read_all_for_order(db: Session, order_id: int):
    # Story #11: View details of a specific order
    return db.query(model.OrderItem).filter(model.OrderItem.order_id == order_id).all()

def delete(db: Session, item_id: int):
    db.query(model.OrderItem).filter(model.OrderItem.id == item_id).delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
