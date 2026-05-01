from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import promo_code as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_promo = model.PromoCode(
        code=request.code,
        discount_pct=request.discount_pct,
        expiration_date=request.expiration_date,
        active=True
    )
    try:
        db.add(new_promo)
        db.commit()
        db.refresh(new_promo)
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_promo


def read_all(db: Session):
    return db.query(model.PromoCode).all()


def read_one(db: Session, item_id: int):
    promo = db.query(model.PromoCode).filter(model.PromoCode.id == item_id).first()
    if not promo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promo code not found!")
    return promo


def update(db: Session, item_id: int, request):
    promo_query = db.query(model.PromoCode).filter(model.PromoCode.id == item_id)
    if not promo_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promo code not found!")

    promo_query.update(request.model_dump(exclude_unset=True))
    db.commit()
    return promo_query.first()


def delete(db: Session, item_id: int):
    promo_query = db.query(model.PromoCode).filter(model.PromoCode.id == item_id)
    if not promo_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promo code not found!")
    promo_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
