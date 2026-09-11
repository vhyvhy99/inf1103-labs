total_inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()
    
    if user_input.lower() == 'quit':
        break

    stock_value = int(user_input)

    if not user_input.isdigit():
        # Checking if it's a negative integer to provide a specific business rule error
        if user_input.startswith('-') and user_input[1:].isdigit():

            print(f"Error: Negative numbers are not allowed. Rejected: {user_input}")
        else:
            print(f"Error: Invalid input. Please enter a valid integer. Rejected: {user_input}")
            
        failed_entries += 1
        continue
    
    total_inventory += stock_value

    if total_inventory > 500:
        print(f"ALERT: Overstock threshold exceeded! Total inventory is {total_inventory} units.")
        break

print("\n--- Audit Report ---")
print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")