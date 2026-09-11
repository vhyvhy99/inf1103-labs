total_inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter a stock quantity (or type 'quit'): ").strip()
    if user_input.lower() == 'quit':
        break

    if not user_input.isdigit():
        if user_input.startswith('-') and user_input[1:].isdigit():
            print("Error: Negative numbers are rejected.")
        else:
            print("Error: Invalid input. Please enter a valid whole number.")  
        failed_entries += 1
        continue

    stock_value = int(user_input)
