def add_item(cart):
    item_name = input("Enter a name of item:").strip()
    try:
        item_price = float(input("Enter a price for {item_name}:"))
        cart[item_name] = item_price
        print(f"{item_name} added to the sucessfully")
    except ValueError:
        print("Invalid price!Please enter a numeric price")

def remove_item(cart):
    item_name = input("Enter the name of item to remove :")
    if item_name in cart:
        del cart[item_name]
        print(f"{item_name} remove succesfully")
    else:
        print(f"{item_name} is not found in cart")

def view_all_bill(cart):
    if not cart:
        print("Your cart is empty")
    else:
        total = sum(cart.values())
        print("\nItem in your cart")
        for item,price in cart.items():
            print(f"- {item}: ${price:.2f}")
        print(f"\nTotal Bill: ${total:.2f}")


def Main():
    cart = {}
    while True:
        print("\nIten Menu:")
        print("1.Add Item")
        print("2.remove Item")
        print("3.view all bill")
        print("4.Exit")

        choice = input("Enter your choice(1-4):")

        if choice == "1":
            add_item(cart)
        elif choice == "2":
            remove_item(cart)
        elif choice == "3":
            view_all_bill(cart)
        elif choice == "4":
            print("Thank you for using the shopping cart system")
        else:
            print("Invalid choice!Please enter a number between 1 to 4")

if __name__ == "__main__":
    Main()