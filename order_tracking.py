# order_tracking.py

orders = {
    "ORD123": "Shipped",
    "ORD124": "Delivered",
    "ORD125": "In Transit",
    "ORD126": "Cancelled"
}

try:
    order_id = input("Enter your Order ID: ").strip().upper()

    if not order_id:
        raise ValueError("Order ID cannot be empty.")

    if order_id not in orders:
        raise KeyError("Order not found. Please check your ID.")

    print(f"📦 Order Status: {orders[order_id]}")

except ValueError as ve:
    print("❌ Input Error:", ve)

except KeyError as ke:
    print("❌ Tracking Error:", ke)

finally:
    print("📌 Order tracking attempt completed.")
