from sqlalchemy import Column, Integer, String
from app.database import Base

class Farmer(Base):
    __tablename__ = "farmers"
    id = Column(Integer, primary_key=True, index=True)
    legal_name = Column(String, nullable=False)
    govt_id = Column(String, unique=True, nullable=False)
    contact_number = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    state_of_residence = Column(String, nullable=False)
    pin_code = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True, index=True)
    owner_name = Column(String, nullable=False)
    phone_no = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    shop_location = Column(String, nullable=False)
    pin_code = Column(String, nullable=False)
    gstin = Column(String, unique=True, nullable=False)
    fssai_license = Column(String, unique=True, nullable=False)

class Individual(Base):
    __tablename__ = "individual"
    id = Column(Integer, primary_key=True, index=True)
    legal_name = Column(String, nullable=False)
    govt_id = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone_no = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    pin_code = Column(Integer, nullable=False)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=False)
    customer_type = Column(String, nullable=False)
    status = Column(String, nullable=False)
