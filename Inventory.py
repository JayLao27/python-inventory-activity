

item_names = []
item_prices = {}

while True:
    print("\n=== INVENTORY MENU ===")
    print("1. Add New Item")
    print("2. Update Item Price")
    print("3. View All Items")
    print("4. Exit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        print("\n--- Add New Item ---")
        name = input("Enter item name: ")
        
       
        if name in item_names:
            print("Error: Item already exists!")
        else:
            price = float(input("Enter item price: $"))
            item_names.append(name)
            item_prices[name] = price
            print(f"Added {name} at ${price:.2f}")
    
    elif choice == "2":
        print("\n--- Update Item Price ---")
        name = input("Enter item name: ")
        
     
        if name in item_names:
            new_price = float(input("Enter new price: $"))
            item_prices[name] = new_price
            print(f"Updated {name} to ${new_price:.2f}")
        else:
            print("Error: Item not found!")
    
    elif choice == "3":
        print("\n--- All Items ---")
        if len(item_names) == 0:
            print("No items in inventory.")
        else:
            for name in item_names:
                print(f"{name}: ${item_prices[name]:.2f}")
    
    elif choice == "4":
        print("\nThank you for using the inventory program!")
        break
    
    else:
        print("Invalid choice. Please try again.")