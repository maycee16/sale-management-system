#!/usr/bin/python3
from sqlalchemy import String, Column, Varchar
class customer(BaseModel, Base):
    """representation of customer """
    _tablename_ = 'customer '
    customer_id=Column(String(40), nullable=False)
    first_name=Column(String(100), nullable=False)
    last_name=Column(String(100), nullable=False)
    email=Column(Varchar(120),nullable=False)
    phone=Column(Varchar(20), nullable=False)
    address=Column(Varchar(300), nullable=False)
    
    def calculate_total(self):
   
