from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/orders", response_model=schemas.OrderResponse)
async def create_order(order_data: schemas.OrderCreate, db: Session = Depends(get_db)):
    new_order = crud.create_order(db, order_data)
    return new_order

@router.get("/orders/active", response_model=list[schemas.OrderResponse])
async def get_active_orders(db: Session = Depends(get_db)):
    active_orders = crud.get_active_orders(db)
    return active_orders
