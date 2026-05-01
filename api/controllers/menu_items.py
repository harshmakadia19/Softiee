from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import menu_item as model, review as review_model, ingredient as ing_model
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func

def create(db: Session, request):
    new_item = model.MenuItem(
        name=request.name,
        description=request.description,
        price=request.price,
        calories=request.calories,
        category=request.category,
        available=True
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return new_item

def read_all(db: Session, category: str = None):
    # Requirement: Search & Filter by category
    query = db.query(model.MenuItem)
    if category:
        query = query.filter(model.MenuItem.category.ilike(f"%{category}%"))
    return query.all()

def read_one(db: Session, item_id: int):
    item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found")
    return item

def update(db: Session, item_id: int, request):
    item_query = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
    if not item_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found")
    item_query.update(request.model_dump(exclude_unset=True))
    db.commit()
    return item_query.first()

def delete(db: Session, item_id: int):
    item_query = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
    if not item_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found")
    item_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Story #3: Alert for insufficient ingredients
def check_stock_alerts(db: Session):
    return db.query(ing_model.Ingredient).filter(ing_model.Ingredient.amount < 10).all()

# Story #15: Identify Unpopular/Low-Rated Dishes
def get_unpopular_dishes(db: Session):
    return db.query(model.MenuItem).join(review_model.Review).group_by(model.MenuItem.id).having(func.avg(review_model.Review.rating) < 3.0).all()

