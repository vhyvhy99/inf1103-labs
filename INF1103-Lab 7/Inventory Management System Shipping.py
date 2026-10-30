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


def add_product_menu(inventory):
    # Handles user input for adding a new product.
    print("\nAdd New Product")
    item_id = input("Product ID: ").strip()

    if inventory.search_product(item_id):
        print("Product ID already exists!")
        return

    print("Select Product Type:")
    print("1. Physical Product")
    print("2. Digital Product")
    p_type = input("Enter choice (1/2): ").strip()

    if p_type not in ["1", "2"]:
        print("Invalid product type selection.")
        return

    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        
        if p_type == "1":
            weight = float(input("Weight (kg): "))
            new_product = PhysicalProduct(item_id, name, price, stock, weight)
        else:
            download_size = float(input("Download Size (MB): "))
            new_product = DigitalProduct(item_id, name, price, stock, download_size)
            
    except ValueError:
        print("Invalid input value entered.")
        return

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
        print("-" * 55)
        product.display_information()
        if isinstance(product, CanBeShipped):
            print(f"Calculated Shipping Cost: ${product.calculate_shipping_cost():.2f}")
        print("-" * 55)
    else:
        print("Product not found.")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM (OOP)")
    print("=" * 40)

    # Initialize sample data if JSON does not exist on first run
    if not os.path.exists(FILENAME):
        default_data = {
            "P001": {"type": "physical", "name": "Laptop", "price": 999.99, "stock": 10, "weight": 2.5},
            "P002": {"type": "digital", "name": "Operating System", "price": 149.99, "stock": 100, "download_size": 4000.0},
            "P003": {"type": "physical", "name": "Headphones", "price": 79.99, "stock": 50, "weight": 0.4}
        }
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