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