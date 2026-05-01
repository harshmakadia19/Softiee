from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, Response, status

from ..models import promo_code as model
from ..schemas import promo_code as schema

def create(db: Session, request: schema.PromoCodeCreate):
    try:
        new_promo_code = model.PromoCode(
            code=request.code,
            discount_pct=request.discount_pct,
            expiration_date=request.expiration_date,
            active=request.active
        )
        db.add(new_promo_code)
        db.commit()
        db.refresh(new_promo_code)
        return new_promo_code
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred while creating promo code.")

def read_all(db: Session):
    return db.query(model.PromoCode).all()

def read_one(db: Session, promo_code_id: int):
    promo_code = db.query(model.PromoCode).filter(model.PromoCode.id == promo_code_id).first()
    if not promo_code:
        raise HTTPException(status_code=404, detail="Promo code not found")
    return promo_code

def update(db: Session, promo_code_id: int, request: schema.PromoCodeUpdate):
    promo_code = read_one(db, promo_code_id)
    
    update_data = request.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(promo_code, key, value)
        
    db.commit()
    db.refresh(promo_code)
    return promo_code

def delete(db: Session, promo_code_id: int):
    promo_code = read_one(db, promo_code_id)
    db.delete(promo_code)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
