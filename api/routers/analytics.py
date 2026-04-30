from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import analytics as controller
from ..dependencies.database import get_db

router = APIRouter(tags=['Staff Analytics'], prefix="/analytics")

@router.get("/revenue/{report_date}")
def daily_revenue(report_date: str, db: Session = Depends(get_db)):
    revenue = controller.get_daily_revenue(db, report_date)
    return {"date": report_date, "total_revenue": revenue if revenue else 0.0}

@router.get("/alerts/low-stock")
def stock_alerts(db: Session = Depends(get_db)):
    return controller.get_stock_alerts(db)

@router.get("/dishes/unpopular")
def unpopular_dishes(db: Session = Depends(get_db)):
    return controller.get_unpopular_dishes(db)