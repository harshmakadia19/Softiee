from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from typing import List

from ..controllers import promo_codes as controller
from ..schemas import promo_code as schema
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/promo-codes",
    tags=['Promo Codes']
)

@router.post("/", response_model=schema.PromoCodeResponse, status_code=status.HTTP_201_CREATED)
def create(request: schema.PromoCodeCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=List[schema.PromoCodeResponse])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{promo_code_id}", response_model=schema.PromoCodeResponse)
def read_one(promo_code_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, promo_code_id)

@router.put("/{promo_code_id}", response_model=schema.PromoCodeResponse)
def update(promo_code_id: int, request: schema.PromoCodeUpdate, db: Session = Depends(get_db)):
    return controller.update(db, promo_code_id, request)

@router.delete("/{promo_code_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(promo_code_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, promo_code_id)
