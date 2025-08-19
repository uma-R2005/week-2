def book_tickets(customer_name, movie_name, *seats):
    if not seats:
        print(f"\n⚠️ No seats selected for {customer_name}'s booking.")
        return

    print(f"\n🎟️ Booking confirmed for {customer_name}!")
    print(f"🎬 Movie: {movie_name}")
    print("💺 Seats booked:", ', '.join(seats))
    print(f"🧾 Total seats: {len(seats)}")


# 🔽 Get input for multiple users
num_customers = 3  # You can change this to 2 or more

for i in range(1, num_customers + 1):
    print(f"\n--- Booking #{i} ---")
    
    customer_name = input("Enter customer name: ")
    movie_name = input("Enter movie name: ")
    seats_input = input("Enter seat numbers (comma-separated, e.g., A1,A2): ")
    
    # Convert seat string to tuple of individual seat IDs
    seats = [seat.strip() for seat in seats_input.split(",") if seat.strip()]

    # Call the booking function with unpacked seat list
    book_tickets(customer_name, movie_name, *seats)
