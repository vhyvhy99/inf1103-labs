# 1. Initialize the inventory and counter variables to zero in the start
total_inventory = 0
failed_entries = 0

# 2. Run in a continuous loop asking user to enter a stock quantity, until the user types quit.
while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()
    
    if user_input.lower() == 'quit':
        break
        
    # 4. Handle invalid input: If the user enters a string (e.g., "ten"), reject it, print an error, 
    # and move to the next iteration. (Hint: use .isdigit()).
    # Note: .isdigit() also handles negative signs by returning False, which helps with rule 5.
    if not user_input.isdigit():
        # Checking if it's a negative integer to provide a specific business rule error
        if user_input.startswith('-') and user_input[1:].isdigit():
            # 5. Enforce business rules: Reject negative numbers.
            print(f"Error: Negative numbers are not allowed. Rejected: {user_input}")
        else:
            print(f"Error: Invalid input. Please enter a valid integer. Rejected: {user_input}")
            
        failed_entries += 1
        continue
        
    # 3. Accept stock values as integers.
    stock_value = int(user_input)
    
    # 6. Manage State: Keep a running total of the inventory.
    total_inventory += stock_value
    
    # 7. Trigger Overstock Alert: If the total inventory exceeds 500 units, print an alert 
    # and break the loop immediately.
    if total_inventory > 500:
        print(f"ALERT: Overstock detected! Total inventory ({total_inventory} units) exceeds 500 units.")
        break

# 8. Reporting: When the user types quit, print the Total Units Processed and the Number of Failed/Rejected Entries.
print("\n--- Audit Report ---")
print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")