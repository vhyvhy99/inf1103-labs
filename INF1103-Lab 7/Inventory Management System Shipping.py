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

# INVENTORY MANAGEMENT

class Inventory:
    # Responsible for managing a collection of Product objects.

    def __init__(self):
        self.products = {}  # Dictionary mapping product_id to Product objects

    def add_product(self, product):
        # Adds a Product object to the inventory collection.
        self.products[product.product_id] = product

    def search_product(self, product_id):
        # Searches for and returns a Product object by its ID, or None if not found.
        return self.products.get(product_id)

    def display_all(self):
        # Displays all products currently in the inventory.
        print("\nCurrent Inventory")
        print("-" * 75)
        if not self.products:
            print("No items in inventory.")
        else:
            for product in self.products.values():
                product.display_information()
        print("-" * 75)


def load_inventory(inventory):
    # Loads inventory data from inventory.json and populates the Inventory object.
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
                for item_id, details in data.items():
                    product_type = details.get("type")
                    
                    if product_type == "physical":
                        product = PhysicalProduct(
                            product_id=item_id,
                            name=details["name"],
                            price=details["price"],
                            stock=details["stock"],
                            weight=details["weight"]
                        )
                    elif product_type == "digital":
                        product = DigitalProduct(
                            product_id=item_id,
                            name=details["name"],
                            price=details["price"],
                            stock=details["stock"],
                            download_size=details["download_size"]
                        )
                    else:
                        continue  # Skip invalid or legacy entries
                        
                    inventory.add_product(product)
                print(f"{FILENAME} found.\nInventory loaded successfully.")
        except json.JSONDecodeError:
            print("Error loading JSON file. Starting with empty inventory.")
    else:
        print(f"{FILENAME} not found. Starting with new inventory.")

def save_inventory(inventory, silent=False):
    # Saves the current inventory collection to inventory.json.
    if not silent:
        print("Saving inventory...")
    
    data = {}
    for item_id, product in inventory.products.items():
        data[item_id] = product.to_dict()

    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
        
    if not silent:
        print(f"Inventory saved successfully to {FILENAME}.")

