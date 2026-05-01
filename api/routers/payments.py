from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import payments as controller
from ..schemas import payment as schema
from ..dependencies.database import get_db

router = APIRouter(tags=['Payments'], prefix="/payments")

@router.post("/", response_model=schema.Payment)
def create(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Payment])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{payment_id}", response_model=schema.Payment)
def read_one(payment_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, payment_id)

@router.delete("/{payment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(payment_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, payment_id)

