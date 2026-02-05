from models.base import Base
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created = Column(DateTime, default=datetime.now)