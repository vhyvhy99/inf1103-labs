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
    
