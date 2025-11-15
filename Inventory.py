item_names = []
item_prices = {}

while True:
    print("\n=== INVENTORY MENU ===")
    print("1. Add New Item")
    print("2. Update Item Price")
    print("3. View All Items")
    print("4. Exit")
    
    choice = input("\nEnter your choice: ").strip()
    
    if choice == "1":
        print("\n--- Add New Item ---")
        name = input("Enter item name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            continue
        if name in item_prices:
            print("Error: Item already exists!")
        else:
            try:
                price = float(input("Enter item price: ").strip())
            except ValueError:
                print("Error: Invalid price.")
                continue
            item_prices[name] = price
            print(f"Added {name} at {price:.2f}")
    
    elif choice == "2":
        print("\n--- Update Item Price ---")
        name = input("Enter item name: ").strip()
        if name in item_prices:
            try:
                new_price = float(input("Enter new price: ").strip())
            except ValueError:
                print("Error: Invalid price.")
                continue
            item_prices[name] = new_price
            print(f"Updated {name} to {new_price:.2f}")
        else:
            print("Error: Item not found!")
    
    elif choice == "3":
        print("\n--- All Items ---")
        if not item_prices:
            print("No items in inventory.")
        else:
            for name in sorted(item_prices):
                print(f"{name}: {item_prices[name]:.2f}")
    
    elif choice == "4":
        print("\nThank you for using the inventory program!")
        break
    
    else:
        print("Invalid choice. Please try again.")