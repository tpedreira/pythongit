# Final Project Inventory Management System
# I needed to reference AI for the For Loops - loops are the once thing I keep having difficulty understanding
# completely in every type of instance. I also have not grasped the concept of Main(). If you recall we had difficulty
# getting main to work a few weeks ago.

inventory = []

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    category = input("Enter item category: ")
    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }
    inventory.append(item)
    print(f"Item '{name}' added successfully!")

def update_item():
    name = input("Enter the name of the item to update: ")
    for item in inventory:
        if item["name"] == name:
            price = input("Enter new price (blank for unchanged): ")
            quantity = input("Enter new quantity (blank for unchanged): ")
            category = input("Enter new category (blank for unchanged): ")
            if price:
                item["price"] = float(price)
            if quantity:
                item["quantity"] = int(quantity)
            if category:
                item["category"] = category
            print(f"Item '{name}' updated!")
            return
    print(f"Item '{name}' not found.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nInventory:")
        for item in inventory:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")
        print()

def remove_item():
    name = input("Enter the name of the item to remove: ")
    for item in inventory:
        if item["name"] == name:
            inventory.remove(item)
            print(f"Item '{name}' removed")
            return
    print(f"Item '{name}' not found.")

def search_by_category():
    category = input("Enter the category to search for: ")
    found_items = [item for item in inventory if item["category"] == category]
    if not found_items:
        print(f"Items not found in category '{category}'.")
    else:
        print(f"\nItems in category '{category}':")
        for item in found_items:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
        print()

while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Update Item")
    print("3. View Inventory")
    print("4. Remove Item")
    print("5. Search by Category")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        update_item()
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        search_by_category()
    elif choice == "6":
        print("Exit Inventory Management System.")
        break
    else:
        print("Choice is Invalid.")
