gittotal_inventory = 0

def get_valid_input():
    user_input = input("Enter a stock quantity (or type 'quit' to exit): ").strip().lower()
    if user_input == 'quit':
        return 'quit'
            
    try:
        value = int(user_input)
        if value < 0:
            print("Invalid input. Quantity cannot be negative.")
            return None
        return value
    except ValueError:
        print("Invalid input. Please enter a valid whole number or 'quit'.")
        return None

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_units, failed_attempts):
    print("\n--- Final Summary Report ---")
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")

def main():
    total_inventory = 0
    total_tax_collected = 0
    successful_deliveries = 0
    failed_attempts = 0

    while True:
        result = get_valid_input()
        
        if result == 'quit':
            break

        if result is None:
            failed_attempts += 1
            continue
            
        total_inventory = process_delivery(total_inventory, result)
        tax = calculate_tax(result)
        total_tax_collected += tax
        successful_deliveries += 1
        
        print(f"Added {result} units to inventory. ")
        print(f"Tax collected: ${tax:.2f}")
        print(f"Running Total Inventory: {total_inventory} units")
        print(f"Total Tax Collected: ${total_tax_collected:.2f}\n")
    generate_report(successful_deliveries, failed_attempts)

if __name__ == "__main__":
    main()