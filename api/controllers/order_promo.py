from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import order_promo as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_link = model.OrderPromo(
        order_id=request.order_id,
        promo_id=request.promo_id
    )
    try:
        db.add(new_link)
        db.commit()
        db.refresh(new_link)
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_link

def read_all(db: Session):
    return db.query(model.OrderPromo).all()

def read_one(db: Session, item_id: int):
    item = db.query(model.OrderPromo).filter(model.OrderPromo.id == item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order Promo link not found!")
    return item

def update(db: Session, item_id: int, request):
    item = db.query(model.OrderPromo).filter(model.OrderPromo.id == item_id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order Promo link not found!")
    item.update(request.model_dump(exclude_unset=True))
    db.commit()
    return item.first()

def delete(db: Session, item_id: int):
    item = db.query(model.OrderPromo).filter(model.OrderPromo.id == item_id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order Promo link not found!")
    item.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)