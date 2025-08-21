import logging
logging.basicConfig(
    filename="bus_reservation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

total_seats = 5
seats = {f"S{i}": None for i in range(1, total_seats + 1)}  # Seat IDs: S1 to S5

def display_seats():
    print("\nAvailable Seats:")
    for seat, name in seats.items():
        status = f"Booked by {name}" if name else "Available"
        print(f"{seat} - {status}")


def book_seat():
    seat_id = input("Enter seat ID to book (e.g. S1): ").strip().upper()
    name = input("Enter your name: ").strip().title()

    if seat_id not in seats:
        print("❌ Invalid seat ID.")
        logging.warning(f"Tried booking invalid seat: {seat_id}")
        return

    if seats[seat_id]:
        print("❌ Seat already booked.")
        logging.warning(f"Attempt to double book {seat_id} by {name}")
    else:
        seats[seat_id] = name
        print(f"✅ Seat {seat_id} booked successfully!")
        logging.info(f"Seat {seat_id} booked by {name}")


def cancel_booking():
    seat_id = input("Enter seat ID to cancel (e.g. S1): ").strip().upper()

    if seat_id not in seats:
        print("❌ Invalid seat ID.")
        logging.warning(f"Tried canceling invalid seat: {seat_id}")
        return

    if seats[seat_id] is None:
        print("❌ Seat is not booked.")
        logging.warning(f"Attempt to cancel unbooked seat {seat_id}")
    else:
        user = seats[seat_id]
        seats[seat_id] = None
        print(f"✅ Booking for seat {seat_id} by {user} cancelled.")
        logging.info(f"Seat {seat_id} cancelled by {user}")


def run_system():
    print("🚌 Welcome to the Bus Reservation System")

    while True:
        print("\n--- Menu ---")
        print("1. View Seats")
        print("2. Book Seat")
        print("3. Cancel Booking")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        try:
            if choice == "1":
                display_seats()
            elif choice == "2":
                book_seat()
            elif choice == "3":
                cancel_booking()
            elif choice == "4":
                print("👋 Thank you for using the system!")
                logging.info("System exited by user.")
                break
            else:
                raise ValueError("Invalid menu choice.")

        except Exception as e:
            print("❌ Error:", e)
            logging.error(f"Unhandled exception: {e}")


if __name__ == "__main__":
    run_system()
