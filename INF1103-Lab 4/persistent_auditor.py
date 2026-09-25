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

def save_inventory(total_inventory, history, total_tax, filename_orders, filename_tax):
    try:
        with open(filename_orders, "w") as f:
            for item in history:
                f.write(f"{item}\n")
        print(f"Order successfully saved to {filename_orders}")
    except Exception as e:
        print(f"Error saving orders: {e}")

    try:
        with open(filename_tax, "w") as f:
            f.write(f"Total Inventory Units: {total_inventory}\n")
            f.write(f"Total Tax Collected: ${total_tax:.2f}\n")
        print(f"Tax calculations saved to {filename_tax}")
    except Exception as e:
        print(f"Error saving tax details: {e}")

def get_valid_input():
    product = input("Enter Product Name: ").strip()
    if product.lower() == "quit":
        return "quit", None

    try:
        quantity = int(input("Enter Quantity: ").strip())
        if quantity < 0:
            print("Invalid input. Quantity cannot be negative.\n")
            return None, None
        return product, quantity
    except ValueError:
        print("Invalid input. Please enter a valid whole number.\n")
        return None, None

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_units, failed_attempts):
    print("\n--- Final Summary Report ---")
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
    
def main():
    total_inventory, transaction_history = load_inventory(ORDERS_FILE)

    total_tax_collected = 0
    successful_deliveries = len(transaction_history)
    failed_attempts = 0

    print("Current Orders:\n")
    if transaction_history:
        for order in transaction_history:
            print(order)
    print()

    next_order_id = 1001 + len(transaction_history)

    while True:
        product, quantity = get_valid_input()

        if product == "quit":
            break

        if product is None or quantity is None:
            failed_attempts += 1
            continue

        total_inventory = process_delivery(total_inventory, quantity)
        tax = calculate_tax(quantity)
        total_tax_collected += tax
        successful_deliveries += 1

        order_line = f"{next_order_id},{product},{quantity}"

        transaction_history.append(order_line)

        print(f"\nNew Order Added:\n{order_line}")
        print(f"Tax collected for entry: ${tax:.2f}")
        print(f"Running Total Inventory: {total_inventory} units\n")

        next_order_id += 1

    generate_report(successful_deliveries, failed_attempts)

    save_inventory(total_inventory, transaction_history, total_tax_collected, ORDERS_FILE, INVENTORY_FILE)

if __name__ == "__main__":
    main()