from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from ..controllers import menu_items as controller
from ..schemas import menu_item as schema
from ..dependencies.database import get_db

router = APIRouter(tags=['Menu Items'], prefix="/menu")

@router.post("/", response_model=schema.MenuItem)
def create(request: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.MenuItem])
def read_all(category: str = Query(None), db: Session = Depends(get_db)):
    return controller.read_all(db, category)

@router.get("/alerts/low-stock")
def get_alerts(db: Session = Depends(get_db)):
    return controller.check_stock_alerts(db)

@router.get("/analytics/unpopular")
def get_unpopular(db: Session = Depends(get_db)):
    return controller.get_unpopular_dishes(db)

@router.get("/{item_id}", response_model=schema.MenuItem)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)

@router.put("/{item_id}", response_model=schema.MenuItem)
def update(item_id: int, request: schema.MenuItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db, item_id, request)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)
