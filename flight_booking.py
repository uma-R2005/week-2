import random

# Flight data
flights = {
    "FL123": {"destination": "New York", "datetime": "2025-09-10 15:30"},
    "FL456": {"destination": "London", "datetime": "2025-09-11 09:00"}
}

# Booking records
bookings = {}

def generate_ref():
    return f"BK{random.randint(1000,9999)}"

def book(name, code, seat, request):
    if code not in flights:
        return None, "Invalid flight code."

    ref = generate_ref()
    bookings[ref] = {
        "name": name,
        "flight": code,
        "seat": seat or "auto",
        "request": request or "none"
    }
    return ref, f"Booking confirmed. Your reference: {ref}"

def view_booking(ref):
    booking = bookings.get(ref)
    if not booking:
        return "No booking found with this reference."
    
    flight = flights[booking["flight"]]
    return (f"\nBooking Details:\n"
            f" Name: {booking['name']}\n"
            f" Flight: {booking['flight']} to {flight['destination']} at {flight['datetime']}\n"
            f" Seat: {booking['seat']}\n"
            f" Special Request: {booking['request']}")

def list_passengers(code):
    if code not in flights:
        return "Invalid flight code."

    passenger_list = [b["name"] for b in bookings.values() if b["flight"] == code]
    if not passenger_list:
        return "No passengers booked on this flight."
    return "\nPassengers:\n" + "\n".join(f"- {p}" for p in passenger_list)

def main():
    print("Flight Booking System")
    while True:
        print("\n1. Book Flight\n2. View Booking\n3. List Passengers\n4. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Name: ")
            print("Flights:")
            for code, info in flights.items():
                print(f" {code}: {info['destination']} at {info['datetime']}")
            code = input("Flight code: ").strip().upper()
            seat = input("Preferred seat (blank = auto): ") or "auto"
            request = input("Special request (optional): ") or "none"
            ref, msg = book(name, code, seat, request)
            print(msg)

        elif choice == "2":
            ref = input("Booking reference: ").strip().upper()
            print(view_booking(ref))

        elif choice == "3":
            code = input("Flight code: ").strip().upper()
            print(list_passengers(code))

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
