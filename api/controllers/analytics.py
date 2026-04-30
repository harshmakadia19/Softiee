from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models import orders as order_model, ingredient as ing_model, review as review_model, menu_item as menu_model

def get_daily_revenue(db: Session, report_date):
    # Requirement: Total revenue generated from food sales on any given day
    return (db.query(func.sum(order_model.Order.total_price))
            .filter(func.date(order_model.Order.created_at) == report_date)
            .scalar())

def get_stock_alerts(db: Session):
    # Requirement: System alert for insufficient ingredients
    return (db.query(ing_model.Ingredient)
            .filter(ing_model.Ingredient.amount < 5)
            .all())

def get_unpopular_dishes(db: Session):
    # Requirement: Identify low-rated or unpopular dishes
    return (db.query(menu_model.MenuItem)
            .join(review_model.Review)
            .group_by(menu_model.MenuItem.id)
            .having(func.avg(review_model.Review.rating) < 3.0)
            .all())