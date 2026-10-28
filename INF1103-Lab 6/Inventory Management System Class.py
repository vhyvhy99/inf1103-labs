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

    def add_product(self, product):
        # Adds a Product object to the inventory collection.
        self.products[product.product_id] = product

    def search_product(self, product_id):
        # Searches for and returns a Product object by its ID, or None if not found.
        return self.products.get(product_id)

    def display_all(self):
        # Displays all products currently in the inventory.
        print("\nCurrent Inventory")
        print("-" * 48)
        if not self.products:
            print("No items in inventory.")
        else:
            for product in self.products.values():
                product.display_information()
        print("-" * 48)


def load_inventory(inventory):
    # Loads inventory data from inventory.json and populates the Inventory object.
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
                for item_id, details in data.items():
                    product = Product(
                        product_id=item_id,
                        name=details["name"],
                        price=details["price"],
                        stock=details["stock"]
                    )
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


def add_product_menu(inventory):
    # Handles user input for adding a new product.
    print("\nAdd New Product")
    item_id = input("Product ID: ").strip()

    if inventory.search_product(item_id):
        print("Product ID already exists!")
        return

    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid price or stock value.")
        return

    new_product = Product(item_id, name, price, stock)
    inventory.add_product(new_product)
    print("Product added successfully!")
