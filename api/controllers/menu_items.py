from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import menu_item as model, review as review_model, ingredient as ing_model
from sqlalchemy import func

def read_all(db: Session, category: str = None):
    query = db.query(model.MenuItem)
    if category:
        # i like handles 'Vegetarian', 'vegetarian', or 'VEGETARIAN'
        query = query.filter(model.MenuItem.category.ilike(f"%{category}%"))
    return query.all()


def update(db: Session, item_id: int, request):
    item_query = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
    item = item_query.first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found")

    # Using model_dump for Pydantic V2 compatibility
    item_query.update(request.model_dump(exclude_unset=True))
    db.commit()
    return item_query.first()


def get_unpopular_dishes(db: Session):
    # Requirement: Identify low-rated dishes (Staff Perspective)
    # This only returns items that HAVE reviews and an average rating < 3.0
    return db.query(model.MenuItem).join(review_model.Review).group_by(model.MenuItem.id).having(
        func.avg(review_model.Review.rating) < 3.0).all()


def check_stock_alerts(db: Session):
    # Requirement: Alert for insufficient ingredients
    return db.query(ing_model.Ingredient).filter(ing_model.Ingredient.amount < 10).all()