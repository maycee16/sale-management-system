!/usr/bin/python3
from sqlalchemy import String, Column, Float, Integer,Varchar
class product (BaseModel, Base):
    """represantation on products"""
    _tablename__='product'
    product_id=Column(String(40), nullable=False)
    product_name=Column(Varchar(40), nullable=False)
    product_description=Column(String(50), nullable=False)
    product_unit=Column(String(50),nullable=False)
    product_price=Column(Float(8,1),nullable=False)
    product_quantity=Column(int(100),nullable=False)
    
    