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
    if not silent:
        print("Saving inventory...")
    with open(FILENAME, "w") as file:
        json.dump(inventory, file, indent=4)
    if not silent:
        print(f"Inventory saved successfully to {FILENAME}.")

def display_all(inventory):
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


def update_stock(inventory):
    print("\nUpdate Stock")
    item_id = input("Enter Product ID: ").strip()

    if item_id in inventory:
        item = inventory[item_id]
        print("\nProduct Found:")
        print(f"Name: {item['name']}")
        print(f"Current Stock: {item['stock']}")
        try:
            new_stock = int(input("New Stock Quantity: "))
            item["stock"] = new_stock
            print("Stock updated successfully!")
        except ValueError:
            print("Invalid input. Stock must be an integer.")
    else:
        print("Product not found.")

def search_product(inventory):
    print("\nSearch Product")
    item_id = input("Enter Product ID: ").strip()

    if item_id in inventory:
        item = inventory[item_id]
        print("\nProduct Found")
        print("-" * 48)
        print(f"ID: {item_id}")
        print(f"Name: {item['name']}")
        print(f"Price: ${item['price']:.2f}")
        print(f"Stock: {item['stock']}")
        print("-" * 48)
    else:
        print("Product not found.")