from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register/farmer")
def register_farmer(farmer: schemas.FarmerCreate, db: Session = Depends(get_db)):
    db_farmer = crud.create_farmer(db, farmer)
    return {"message": "Farmer registered successfully", "id": db_farmer.id}

@router.post("/register/restaurant")
def register_restaurant(restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db)):
    db_restaurant = crud.create_restaurant(db, restaurant)
    return {"message": "Restaurant registered successfully", "id": db_restaurant.id}

@router.post("/register/individual")
def register_individual(individual: schemas.IndividualCreate, db: Session = Depends(get_db)):
    db_individual = crud.create_individual(db, individual)
    return {"message": "Individual registered successfully", "id": db_individual.id}

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.authenticate_user(db, user.phone_no, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful", **db_user}
