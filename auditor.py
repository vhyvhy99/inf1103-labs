total_inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter a stock quantity (or type 'quit'): ").strip()
    if user_input.lower() == 'quit':
        break

stock_value = int(user_input)
