from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from ..controllers import menu_items as controller
from ..schemas import menu_item as schema
from ..dependencies.database import get_db
from typing import Optional

router = APIRouter(tags=['Menu Items'], prefix="/menu")

# 1. FIXED: Specific paths must come BEFORE /{item_id}
@router.get("/alerts/low-stock")
def get_alerts(db: Session = Depends(get_db)):
    return controller.check_stock_alerts(db)

@router.get("/analytics/unpopular")
def get_unpopular(db: Session = Depends(get_db)):
    return controller.get_unpopular_dishes(db)

# 2. Main Menu / Search Logic
@router.get("/", response_model=list[schema.MenuItem])
def read_all(category: Optional[str] = Query(None, description="Optional: Filter by category (e.g. Vegetarian)"), db: Session = Depends(get_db)):
    # If you leave the category box empty and hit 'Execute', it returns everything.
    return controller.read_all(db, category)

# 3. Generic ID paths go at the BOTTOM
@router.get("/{item_id}", response_model=schema.MenuItem)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)

@router.post("/", response_model=schema.MenuItem, status_code=status.HTTP_201_CREATED)
def create(request: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.put("/{item_id}", response_model=schema.MenuItem)
def update(item_id: int, request: schema.MenuItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db, item_id, request)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)