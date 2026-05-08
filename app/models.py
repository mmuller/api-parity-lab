# models
from sqlalchemy import Column, Integer, String, Float
from .db import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer = Column(String)
    amount = Column(Float)
    status = Column(String)
    