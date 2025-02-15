from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/login", response_model=schemas.UserLoginResponse)
async def login_user(login_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user_type, user = crud.authenticate_user(db, login_data.phone_no, login_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "user_type": user_type,
        "user_details": user  # ✅ Securely returns user data without password
    }


# ✅ Register a Farmer
@router.post("/users/register/farmer")
async def register_farmer(farmer_data: schemas.FarmerCreate, db: Session = Depends(get_db)):
    existing_user, _ = crud.get_user_by_phone(db, farmer_data.contact_number)
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone number already registered")

    new_farmer = crud.create_farmer(db, farmer_data)
    return {"message": "Farmer registered successfully", "id": new_farmer.id}

# ✅ Register a Restaurant
@router.post("/users/register/restaurant")
async def register_restaurant(restaurant_data: schemas.RestaurantCreate, db: Session = Depends(get_db)):
    existing_user, _ = crud.get_user_by_phone(db, restaurant_data.phone_no)
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone number already registered")

    new_restaurant = crud.create_restaurant(db, restaurant_data)
    return {"message": "Restaurant registered successfully", "id": new_restaurant.id}

# ✅ Register an Individual
@router.post("/users/register/individual")
async def register_individual(individual_data: schemas.IndividualCreate, db: Session = Depends(get_db)):
    existing_user, _ = crud.get_user_by_phone(db, individual_data.phone_no)
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone number already registered")

    new_individual = crud.create_individual(db, individual_data)
    return {"message": "Individual registered successfully", "id": new_individual.id}
