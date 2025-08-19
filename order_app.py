# Function to place a food order with any number of items
def place_order(customer_name, *items):
    if not items:
        print(f"\n⚠️ No items selected for {customer_name}'s order.")
        return
    
    print(f"\n✅ Order placed successfully for {customer_name}!")
    print("🍽️ Items ordered:")
    for item in items:
        print(f"- {item}")
    
    print(f"🛒 Total items: {len(items)}")


# 🔽 Example 1: Uma orders 3 items
place_order("Uma", "Pizza", "Burger", "Coke")

# 🔽 Example 2: Alex orders South Indian food
place_order("Alex", "Idli", "Dosa", "Sambar", "Filter Coffee")

# 🔽 Example 3: Ravi tries to order with no items
place_order("Ravi")

# 🔽 Example 4: Maya orders a dessert
place_order("Maya", "Gulab Jamun")
