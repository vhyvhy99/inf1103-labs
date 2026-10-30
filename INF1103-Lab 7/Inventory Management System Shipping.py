from abc import ABC, abstractmethod
import json
import os

FILENAME = "inventory.json"

# ABSTRACT BASE CLASS

    def update_stock(self, new_stock): 
        # Updates the stock quantity with internal control (encapsulation).
        self._stock = new_stock

    def display_information(self):
        # Displays formatted information for this specific product.
        print(f"ID: {self._product_id} | Name: {self.name} | Price: ${self._price:.2f} | Stock: {self._stock}", end="")

    @abstractmethod
    def get_fulfilment_info(self):
        """Abstract method to return fulfilment information."""
        pass

    @abstractmethod
    def to_dict(self):
        """Converts the Product object into a dictionary for JSON serialization."""
        pass

# INTERFACE

class CanBeShipped(ABC):
    """Interface-style abstract base class for products that can be shipped."""

    @abstractmethod
    def calculate_shipping_cost(self):
        """Calculates and returns the shipping cost."""
        pass

# SUBCLASSES

class PhysicalProduct(Product, CanBeShipped):
    """Represents a physical product that has weight and can be shipped."""

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.weight = weight

    def display_information(self):
        super().display_information()
        print(f" | Weight: {self.weight} kg | Fulfilment: {self.get_fulfilment_info()}")

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        # Example rule: Base shipping cost + cost per kg
        base_rate = 5.00
        per_kg_rate = 2.50
        return base_rate + (self.weight * per_kg_rate)

    def to_dict(self):
        return {
            "type": "physical",
            "name": self.name,
            "price": self._price,
            "stock": self._stock,
            "weight": self.weight
        }


class DigitalProduct(Product):
    """Represents a digital product that has a download size."""

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.download_size = download_size

    def display_information(self):
        super().display_information()
        print(f" | Download Size: {self.download_size} MB | Fulfilment: {self.get_fulfilment_info()}")

    def get_fulfilment_info(self):
        return "Delivered digitally via download link."

    def to_dict(self):
        return {
            "type": "digital",
            "name": self.name,
            "price": self._price,
            "stock": self._stock,
            "download_size": self.download_size
        }

