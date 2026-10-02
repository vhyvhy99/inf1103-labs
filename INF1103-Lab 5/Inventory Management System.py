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
