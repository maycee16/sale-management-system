#!/usr/bin/python3
from sqlalchemy import String, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sales(Base):
    """Representation of sales"""
    __tablename__ = 'sales'

    sales_id = Column(String(30), primary_key=True, nullable=False)
    opening_stock = Column(String(50), nullable=False)
    product_name = Column(String(50), nullable=False)
    quantity_sold = Column(Integer, nullable=False)
    revenue = Column(Float, nullable=False)
    closing_stock = Column(Float, nullable=False)

    def calculate_revenue(self):
        return self.quantity_sold * self.revenue

    def calculate_closing_stock(self):
        return float(self.opening_stock) - self.quantity_sold            