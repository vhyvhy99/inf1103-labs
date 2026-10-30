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