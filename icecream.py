# Ice Cream Vending Machine Simulator

# Initial Inventory (Flavor: [Price, Stock])
inventory = {
    "Vanilla": [50, 10],
    "Chocolate": [60, 8],
    "Strawberry": [55, 5],
    "Mango": [65, 7]
}

# Function to display menu
def show_menu():
    print("\n--- Ice Cream Vending Machine ---")
    print("Available Flavors:")
    for i, (flavor, (price, stock)) in enumerate(inventory.items(), 1):
        print(f"{i}. {flavor} - Rs.{price} (Stock: {stock})")
    print(f"{len(inventory)+1}. Exit")

# Function to take order
def order_ice_cream():
    show_menu()
    choice = input("Select flavor number: ")
    try:
        choice = int(choice)
        if choice == len(inventory) + 1:
            print("Exiting...")
            return False
        elif 1 <= choice <= len(inventory):
            flavor = list(inventory.keys())[choice - 1]
            price, stock = inventory[flavor]
            if stock == 0:
                print(f"Sorry, {flavor} is out of stock!")
                return True
            qty = int(input(f"How many {flavor} cones? "))
            if qty <= 0:
                print("Invalid quantity!")
            elif qty > stock:
                print(f"Sorry, only {stock} left in stock!")
            else:
                total = price * qty
                print(f"Total amount: Rs.{total}")
                pay = int(input("Enter payment amount: "))
                if pay < total:
                    print("Insufficient payment. Order canceled.")
                else:
                    inventory[flavor][1] -= qty
                    change = pay - total
                    print(f"Order successful! Your {qty} {flavor} cone(s). Change: Rs.{change}")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return True

# Function to restock ice cream (admin)
def restock():
    print("\n--- Restock Menu ---")
    for i, flavor in enumerate(inventory.keys(), 1):
        print(f"{i}. {flavor}")
    try:
        choice = int(input("Select flavor number to restock: "))
        if 1 <= choice <= len(inventory):
            flavor = list(inventory.keys())[choice - 1]
            qty = int(input(f"Enter quantity to add to {flavor}: "))
            if qty > 0:
                inventory[flavor][1] += qty
                print(f"{flavor} stock updated. New stock: {inventory[flavor][1]}")
            else:
                print("Invalid quantity!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input!")

# Main Loop
def main():
    while True:
        print("\n1. Order Ice Cream")
        print("2. Restock Ice Cream (Admin)")
        print("3. View Inventory")
        print("4. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            if not order_ice_cream():
                break
        elif choice == "2":
            restock()
        elif choice == "3":
            print("\n--- Current Inventory ---")
            for flavor, (price, stock) in inventory.items():
                print(f"{flavor} - Rs.{price} (Stock: {stock})")
        elif choice == "4":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
