#!/usr/bin/python3
"""This module creates the Purchase class"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float

class Purchase(BaseModel, Base):
    """A class named Purchase
    Attributes:
    attr1(item_name): name of the purchased item
    attr2(quantity): quantity of the purchased item
    attr3(price_per_unit): price per unit of the purchased item
    """
    __tablename__ = 'purchases'
    item_name = Column(String(120), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_per_unit = Column(Float, nullable=False)

    def calculate_total(self):
        """Calculates the total cost of the purchase"""
        return self.quantity * self.price_per_unit