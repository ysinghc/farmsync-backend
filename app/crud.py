from sqlalchemy.orm import Session
from app.models import Farmer, Restaurant, Individual, Order
from app.security import verify_password, hash_password
from app.schemas import FarmerResponse, RestaurantResponse, IndividualResponse, OrderCreate, OrderResponse

# ✅ Authenticate User Without Returning Password
def authenticate_user(db: Session, phone_no: str, password: str):
    user_type, user_obj = get_user_by_phone(db, phone_no)

    if not user_obj or not verify_password(password, user_obj.password):
        return None, None  # Invalid credentials

    # Convert SQLAlchemy model to corresponding Pydantic response model
    if user_type == "farmer":
        user_response = FarmerResponse.model_validate(user_obj)
    elif user_type == "restaurant":
        user_response = RestaurantResponse.model_validate(user_obj)
    elif user_type == "individual":
        user_response = IndividualResponse.model_validate(user_obj)
    else:
        return None, None  # Invalid user type

    return user_type, user_response


def get_user_by_phone(db: Session, phone_no: str):
    """Fetch full user object including password for authentication"""
    user = db.query(Farmer).filter(Farmer.contact_number == phone_no).first()
    if user:
        return "farmer", user

    user = db.query(Restaurant).filter(Restaurant.phone_no == phone_no).first()
    if user:
        return "restaurant", user

    user = db.query(Individual).filter(Individual.phone_no == phone_no).first()
    if user:
        return "individual", user

    return None, None  # No user found


# ✅ Create a new farmer
def create_farmer(db: Session, farmer_data):
    hashed_password = hash_password(farmer_data.password)
    farmer_dict = farmer_data.dict()
    farmer_dict.pop("password")
    db_farmer = Farmer(**farmer_dict, password=hashed_password)
    db.add(db_farmer)
    db.commit()
    db.refresh(db_farmer)
    return db_farmer

# ✅ Create a new restaurant
def create_restaurant(db: Session, restaurant_data):
    hashed_password = hash_password(restaurant_data.password)
    restaurant_dict = restaurant_data.dict()
    restaurant_dict.pop("password")
    db_restaurant = Restaurant(**restaurant_dict, password=hashed_password)
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

# ✅ Create a new individual
def create_individual(db: Session, individual_data):
    hashed_password = hash_password(individual_data.password)
    individual_dict = individual_data.dict()
    individual_dict.pop("password")
    db_individual = Individual(**individual_dict, password=hashed_password)
    db.add(db_individual)
    db.commit()
    db.refresh(db_individual)
    return db_individual

# Create a new order
def create_order(db: Session, order_data: OrderCreate):
    db_order = Order(**order_data.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Retrieve active orders
def get_active_orders(db: Session):
    return db.query(Order).filter(Order.status == "active").all()
