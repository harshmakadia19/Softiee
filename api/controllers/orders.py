from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import orders as model
from sqlalchemy.exc import SQLAlchemyError
import secrets
import string


def generate_tracking_number(length=12):
    # Generates a unique alphanumeric string for the VARCHAR(36) field
    chars = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))


def create(db: Session, request):
    # Requirement: Align fields with model
    new_item = model.Order(
        customer_id=request.customer_id,
        tracking_number=generate_tracking_number(),  # System generated unique string
        status=request.status,
        order_type=request.order_type,
        total_price=request.total_price
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        return db.query(model.Order).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


def read_one(db: Session, item_id):
    item = db.query(model.Order).filter(model.Order.id == item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")
    return item


def update(db: Session, item_id, request):
    try:
        item_query = db.query(model.Order).filter(model.Order.id == item_id)
        if not item_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")

        # Uses .dict() to handle Pydantic schema validation correctly
        update_data = request.dict(exclude_unset=True)
        item_query.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return item_query.first()


def delete(db: Session, item_id):
    try:
        item_query = db.query(model.Order).filter(model.Order.id == item_id)
        if not item_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")
        item_query.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return Response(status_code=status.HTTP_204_NO_CONTENT)