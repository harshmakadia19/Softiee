from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import review as model
from datetime import datetime, UTC

def create(db: Session, request):
    new_review = model.Review(
        order_id=request.order_id,
        menu_item_id=request.menu_item_id,
        rating=request.rating,
        review_text=request.review_text,
        created_at=datetime.now(UTC) #
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review

def read_all(db: Session, menu_item_id: int = None):
    # Requirement: View reviews per dish
    query = db.query(model.Review)
    if menu_item_id:
        query = query.filter(model.Review.menu_item_id == menu_item_id)
    return query.all()

def read_one(db: Session, review_id: int):
    review = db.query(model.Review).filter(model.Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    return review

def update(db: Session, review_id: int, request):
    query = db.query(model.Review).filter(model.Review.id == review_id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    query.update(request.model_dump(exclude_unset=True))
    db.commit()
    return query.first()

def delete(db: Session, review_id: int):
    query = db.query(model.Review).filter(model.Review.id == review_id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

