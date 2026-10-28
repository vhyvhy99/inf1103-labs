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


def update_stock_menu(inventory):
    # Handles user input for updating product stock.
    print("\nUpdate Stock")
    item_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(item_id)
    if product:
        print("\nProduct Found:")
        print(f"Name: {product.name}")
        print(f"Current Stock: {product.stock}")
        try:
            new_stock = int(input("New Stock Quantity: "))
            product.update_stock(new_stock)
            print("Stock updated successfully!")
        except ValueError:
            print("Invalid input. Stock must be an integer.")
    else:
        print("Product not found.")


def search_product_menu(inventory):
    # Handles user input for searching a product.
    print("\nSearch Product")
    item_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(item_id)
    if product:
        print("\nProduct Found")
        print("-" * 48)
        print(f"ID: {product.product_id}")
        print(f"Name: {product.name}")
        print(f"Price: ${product.price:.2f}")
        print(f"Stock: {product.stock}")
        print("-" * 48)
    else:
        print("Product not found.")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM (OOP)")
    print("=" * 40)

    # Initialize sample data if JSON does not exist on first run
    if not os.path.exists(FILENAME):
    
        with open(FILENAME, "w") as f:
            json.dump(default_data, f, indent=4)

    inventory = Inventory()
    load_inventory(inventory)

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        choice = input("Enter option: ").strip()

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product_menu(inventory)
        elif choice == "3":
            update_stock_menu(inventory)
        elif choice == "4":
            search_product_menu(inventory)
        elif choice == "5":
            save_inventory(inventory)
        elif choice == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory, silent=True)
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()