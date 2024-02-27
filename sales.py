#!/usr/bin/python3
from sqlalchemy import String, Column, Primarykey, integer
class sales(BaseModel, Base):
    """representation of sales """
    _tablename_ = 'sales '
sales_id = Column(String(30), Primarykey ('sales.id'), nullable=False )
opening_stock=Column(String(50), nullable=False)
product_name=Column(String(50), nullable=False)
quantity_sold=Column(integer, nullable=False)
revenue=Column(float, nullable=False)
closing_stock=Column(float, nullable=False)
def calculate_revenue(self):
    return self.quantity_sold * self.revenu
def calculate_closing_stock(self):
     return float(self.opening_stock) - self.quantity_sold
 

            