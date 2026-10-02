import json
import os

FILENAME = "inventory.json"

def load_inventory():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                inventory = json.load(file)
                print(f"{FILENAME} found.\nInventory loaded successfully.")
                return inventory
        except json.JSONDecodeError:
            print("Error loading JSON file. Starting with empty inventory.")
            return {}
    else:
        print(f"{FILENAME} not found. Starting with new inventory.")
        return {}

def save_inventory(inventory, silent=False):
    """Save inventory dictionary to inventory.json."""
    if not silent:
        print("Saving inventory...")
    with open(FILENAME, "w") as file:
        json.dump(inventory, file, indent=4)
    if not silent:
        print(f"Inventory saved successfully to {FILENAME}.")

def display_all(inventory):
    """Option 1: Display all products in inventory."""
    print("\nCurrent Inventory")
    print("-" * 48)
    if not inventory:
        print("No items in inventory.")
    else:
        for item_id, details in inventory.items():
            price = details["price"]
            stock = details["stock"]
            name = details["name"]
            print(
                f"ID: {item_id} | Name: {name} | Price: ${price:.2f} | Stock: {stock}"
            )
    print("-" * 48)

def add_product(inventory):
    """Option 2: Add a new product to inventory."""
    print("\nAdd New Product")
    item_id = input("Product ID: ").strip()

    if item_id in inventory:
        print("Product ID already exists!")
        return

    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid price or stock value.")
        return

    inventory[item_id] = {"name": name, "price": price, "stock": stock}
    print("Product added successfully!")