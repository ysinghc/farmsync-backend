from pydantic import BaseModel
from typing import Optional

class FarmerCreate(BaseModel):
    legal_name: str
    govt_id: str
    contact_number: str
    age: int
    state_of_residence: str
    pin_code: int
    address: str
    password: str

class RestaurantCreate(BaseModel):
    owner_name: str
    phone_no: str
    password: str
    age: int
    shop_location: str
    pin_code: str
    gstin: str
    fssai_license: str

class IndividualCreate(BaseModel):
    legal_name: str
    govt_id: str
    password: str
    phone_no: str
    age: int
    address: str
    pin_code: int


# ✅ Response Model for Farmer (Excludes Password)
class FarmerResponse(BaseModel):
    id: int
    legal_name: str
    govt_id: str
    contact_number: str
    age: int
    state_of_residence: str
    pin_code: int
    address: str

    class Config:
        from_attributes = True  # ✅ Fix for FastAPI 0.95+

# ✅ Response Model for Restaurant (Excludes Password)
class RestaurantResponse(BaseModel):
    id: int
    owner_name: str
    phone_no: str
    age: int
    shop_location: str
    pin_code: str
    gstin: str
    fssai_license: str

    class Config:
        from_attributes = True  # ✅ Fix for FastAPI 0.95+

# ✅ Response Model for Individual (Excludes Password)
class IndividualResponse(BaseModel):
    id: int
    legal_name: str
    govt_id: str
    phone_no: str
    age: int
    address: str
    pin_code: int

    class Config:
        from_attributes = True  # ✅ Fix for FastAPI 0.95+

# ✅ Login Request Schema
class UserLogin(BaseModel):
    phone_no: str
    password: str

# ✅ Login Response Schema
class UserLoginResponse(BaseModel):
    user_type: str
    user_details: Optional[FarmerResponse | RestaurantResponse | IndividualResponse]

# Schema for creating a new order
class OrderCreate(BaseModel):
    customer_id: int
    customer_type: str
    status: str

# Schema for retrieving order details
class OrderResponse(BaseModel):
    id: int
    customer_id: int
    customer_type: str
    status: str

    class Config:
        from_attributes = True
