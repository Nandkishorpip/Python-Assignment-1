class InventoryManagement:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, price, quantity):
        if item_name in self.inventory:
            print(f"{item_name} already exists. Use update to modify it.")
        else:
            self.inventory[item_name] = {'price': price, 'quantity': quantity}
            print(f"Item {item_name} added successfully.")

    def update_item(self, item_name, price=None, quantity=None):
        if item_name in self.inventory:
            if price is not None:
                self.inventory[item_name]['price'] = price
            if quantity is not None:
                self.inventory[item_name]['quantity'] += quantity
            print(f"Item {item_name} updated successfully.")
        else:
            print(f"Item {item_name} does not exist in the inventory.")

    def delete_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"Item {item_name} deleted successfully.")
        else:
            print(f"Item {item_name} does not exist in the inventory.")

    def view_inventory(self):
        if not self.inventory:
            print("The inventory is empty.")
        else:
            print("Current Inventory:")
            print("-" * 35)
            print("{:<15} {:<10} {:<10}".format("Item Name", "Price", "Quantity"))
            print("-" * 35)
            for item_name, details in self.inventory.items():
                print("{:<15} {:<10} {:<10}".format(
                    item_name, details['price'], details['quantity']
                ))
            print("-" * 35)

# Main program
if __name__ == "__main__":
    store = InventoryManagement()

    while True:
        print("\n--- Inventory Management ---")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. View Inventory")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter item name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            store.add_item(name, price, quantity)
        elif choice == 2:
            name = input("Enter item name: ")
            price = input("Enter new price (or press Enter to skip): ")
            quantity = input("Enter additional quantity (or press Enter to skip): ")
            price = float(price) if price else None
            quantity = int(quantity) if quantity else None
            store.update_item(name, price, quantity)
        elif choice == 3:
            name = input("Enter item name: ")
            store.delete_item(name)
        elif choice == 4:
            store.view_inventory()
        elif choice == 5:
            print("Exiting Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")