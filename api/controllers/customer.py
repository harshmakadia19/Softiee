from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import customer as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_customer = model.Customer(
        name=request.name,
        email=request.email,
        phone=request.phone,
        address=request.address
    )
    try:
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return new_customer

def read_all(db: Session):
    return db.query(model.Customer).all()

def read_one(db: Session, item_id: int):
    item = db.query(model.Customer).filter(model.Customer.id == item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found!")
    return item

def update(db: Session, item_id: int, request):
    item = db.query(model.Customer).filter(model.Customer.id == item_id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found!")
    item.update(request.dict(exclude_unset=True))
    db.commit()
    return item.first()

def delete(db: Session, item_id: int):
    item = db.query(model.Customer).filter(model.Customer.id == item_id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found!")
    item.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
