# 1. Initialize the inventory and counter variables to zero in the start
total_inventory = 0
failed_entries = 0

# 2. Run in a continuous loop asking user to enter a stock quantity, until the user types quit.
while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()
    
    if user_input.lower() == 'quit':
        break

# 3. Accept stock values as integers.
    stock_value = int(user_input)
