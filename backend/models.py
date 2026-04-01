from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    """用户模型"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Itinerary(Base):
    """行程模型"""
    __tablename__ = "itineraries"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    start_location = Column(String(255), nullable=False)
    destination = Column(String(255), nullable=False)
    days = Column(Integer, nullable=False)
    budget = Column(String(50), nullable=False)
    overview = Column(Text, nullable=False)  # JSON格式存储
    daily_plan = Column(Text, nullable=False)  # JSON格式存储
    budget_breakdown = Column(Text, nullable=False)  # JSON格式存储
    packing_list = Column(Text, nullable=False)  # JSON格式存储
    weather_alert = Column(Text, nullable=True)  # JSON格式存储
    model_info = Column(Text, nullable=True)  # JSON格式存储
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
