import json
import os

FILENAME = "inventory.json"

class Product: 
    # Represents an individual product with encapsulated attributes and specific behaviors.
    
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self.name = name
        self._price = price
        self._stock = stock

    @property
    def product_id(self):
        return self._product_id

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    def update_stock(self, new_stock): 
        #Updates the stock quantity with internal control (encapsulation).
        self._stock = new_stock

    def display_information(self):
        # Displays formatted information for this specific product.
        print(f"ID: {self._product_id} | Name: {self.name} | Price: ${self._price:.2f} | Stock: {self._stock}")

    def to_dict(self):
        # Converts the Product object into a dictionary for JSON serialization.
        return {
            "name": self.name,
            "price": self._price,
            "stock": self._stock
        }


class Inventory:
    # Responsible for managing a collection of Product objects.

    def __init__(self):
        self.products = {}  # Dictionary mapping product_id to Product objects
