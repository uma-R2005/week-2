# billing.py

menu = {
    "Pizza": 250,
    "Burger": 120,
    "Coke": 40
}

try:
    item = input("Enter item name: ").title()

    if item not in menu:
        raise KeyError("Item not available on the menu!")

    qty = int(input("Enter quantity: "))
    if qty <= 0:
        raise ValueError("Quantity must be positive.")

    total = menu[item] * qty
    print(f"\nTotal for {item} x {qty} = ₹{total}")

except KeyError as e:
    print("Error:", e)

except ValueError as ve:
    print("Invalid input:", ve)

finally:
    print("\nThank you for visiting!")
