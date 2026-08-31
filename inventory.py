# Inventory program

inventory={
    "ipads":{"price": 649.00, "quantity": 50},
    "ipods":{"price": 149.00, "quantity": 75},
    "iphones":{"price": 1049.00, "quantity": 100},
    "phone chargers":{"price": 29.99, "quantity": 225}
}


# Set to track low-stock items (quantity < 10)
low_stock=set()

def update_low_stock():
    """Refresh the low-stock set based on current quantities."""
    low_stock.clear()
    for product, info in inventory.items():
        if info["quantity"] < 10:
            low_stock.add(product)


def display_inventory():
    """Print the inventory in a formatted table."""
    print("\n========================================")
    print("             Current Inventory")
    print("========================================")
    print(f"{'Product':<20} {'Price':<10} {'Qty':<10} {'Value':<10}")
    print("-" * 55)

    total_value = 0

    for product, info in inventory.items():
        price = info["price"]
        qty = info["quantity"]
        value = price * qty
        total_value += value

        print(f"{product:<20} ${price:<9.2f} {qty:<10} ${value:<10.2f}")

    print("-" * 55)
    print(f"Total Inventory Value: ${total_value:.2f}")

    update_low_stock()
    print(f"Low-stock items (<10): {low_stock if low_stock else 'None'}\n")


def lookup_product():
    """Let the user look up a product safely using .get()."""
    name = input("Enter product name to look up: ").lower()
    product = inventory.get(name)

    if product:
        print(f"\n{name.title()} details:")
        print(f"Price: ${product['price']}")
        print(f"Quantity: {product['quantity']}\n")
    else:
        print("\nProduct not found.\n")


def update_quantity():
    """Let the user update the quantity of a product."""
    name = input("Enter product name to update: ").lower()

    if name not in inventory:
        print("\nProduct not found.\n")
        return

    try:
        change = int(input("Enter quantity change (negative for sale, positive for restock): "))
        inventory[name]["quantity"] += change
        print(f"\nUpdated {name}: quantity is now {inventory[name]['quantity']}\n")
    except ValueError:
        print("\nInvalid number entered.\n")


# Main loop
while True:
    display_inventory()

    print("What would you like to do?")
    print("1. Look up a product")
    print("2. Update product quantity")
    print("3. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        lookup_product()
    elif choice == "2":
        update_quantity()
    elif choice == "3":
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid choice.\n")