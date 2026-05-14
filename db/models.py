from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from datetime import datetime
from db.database import Base

# USERS
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    username = Column(String, unique=True)
    phone = Column(String, unique=True)
    password = Column(String)
    state = Column(String)
    lga = Column(String)
    role = Column(String, default="buyer")  # buyer only system
    created_at = Column(DateTime, default=datetime.utcnow)

# WALLET
class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    balance = Column(Float, default=0.0)

# PRODUCTS
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)
    unit = Column(String)
    image_url = Column(String)
    location = Column(String)
    available_qty = Column(Float)

# COOPERATIVES
class Cooperative(Base):
    __tablename__ = "cooperatives"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    product_category = Column(String)
    target_qty = Column(Float)
    max_members = Column(Integer)
    contribution_per_member = Column(Float)
    status = Column(String, default="funding")