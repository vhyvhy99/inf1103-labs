ORDERS_FILE = "orders.txt"
INVENTORY_FILE = "inventory.txt"

def load_inventory(filename=ORDERS_FILE):
    history = []
    total_inventory = 0

    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    history.append(line)
                    parts = line.split(",")
                    if len(parts) >= 3 and parts[-1].strip().isdigit():
                        total_inventory += int(parts[-1].strip())
    except FileNotFoundError:
        pass 

    return total_inventory, history