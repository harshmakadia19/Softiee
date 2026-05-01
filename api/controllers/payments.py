from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import payment as model
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, UTC


def create(db: Session, request):
    # Ensure all required fields from your model are present
    new_payment = model.Payment(
        order_id=request.order_id,
        payment_type=request.payment_type,
        card_last4=request.card_last4,
        status="COMPLETED",
        amount=request.amount,
        paid_at=datetime.now(UTC)  # Modern UTC format
    )
    try:
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_payment


def read_all(db: Session):
    return db.query(model.Payment).all()


def read_one(db: Session, payment_id: int):
    payment = db.query(model.Payment).filter(model.Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment record not found")
    return payment


def update(db: Session, payment_id: int, request):
    try:
        query = db.query(model.Payment).filter(model.Payment.id == payment_id)
        if not query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment record not found")

        # Use model_dump to keep Pydantic happy
        query.update(request.model_dump(exclude_unset=True), synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return query.first()


def delete(db: Session, payment_id: int):
    try:
        query = db.query(model.Payment).filter(model.Payment.id == payment_id)
        if not query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment record not found")
        query.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return Response(status_code=status.HTTP_204_NO_CONTENT)