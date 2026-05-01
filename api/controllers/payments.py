from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import payment as model
from datetime import datetime

def create(db: Session, request):
    new_payment = model.Payment(
        order_id=request.order_id,
        payment_type=request.payment_type, #
        card_last4=request.card_last4,
        status="COMPLETED",
        amount=request.amount,
        paid_at=datetime.utcnow()
    )
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment

def read_all(db: Session):
    return db.query(model.Payment).all()

def read_one(db: Session, payment_id: int):
    payment = db.query(model.Payment).filter(model.Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment record not found")
    return payment

def update(db: Session, payment_id: int, request):
    # Primarily used to update transaction status if needed
    query = db.query(model.Payment).filter(model.Payment.id == payment_id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment record not found")
    query.update(request.dict(exclude_unset=True))
    db.commit()
    return query.first()

def delete(db: Session, payment_id: int):
    query = db.query(model.Payment).filter(model.Payment.id == payment_id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment record not found")
    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
