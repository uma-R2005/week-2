import logging

# -------------------------------
# Configure Logging
# -------------------------------
logging.basicConfig(
    filename="library_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------------------
# Sample Book Database
# -------------------------------
books = {
    "Python101": True,
    "AI_Basics": True,
    "DataScience": True,
    "FlaskGuide": True,
    "ML_Fundamentals": True
}

# -------------------------------
# Functions
# -------------------------------
def display_books():
    print("\n📚 Available Books:")
    for title, available in books.items():
        status = "✅ Available" if available else "❌ Borrowed"
        print(f" - {title}: {status}")

def borrow_book():
    book = input("Enter book title to borrow: ").strip()
    if book not in books:
        print("❌ Book not found in library.")
        logging.warning(f"Attempted to borrow non-existent book: {book}")
    elif not books[book]:
        print("❌ Book is already borrowed.")
        logging.warning(f"Attempted to borrow unavailable book: {book}")
    else:
        books[book] = False
        print(f"✅ You have borrowed '{book}'.")
        logging.info(f"Book borrowed: {book}")

def return_book():
    book = input("Enter book title to return: ").strip()
    if book not in books:
        print("❌ Book not found in library.")
        logging.warning(f"Attempted to return non-existent book: {book}")
    elif books[book]:
        print("❌ Book was not borrowed.")
        logging.warning(f"Attempted to return a book that wasn't borrowed: {book}")
    else:
        books[book] = True
        print(f"✅ You have returned '{book}'.")
        logging.info(f"Book returned: {book}")

# -------------------------------
# Run the System
# -------------------------------
def run_library():
    print("📖 Welcome to the Library System")

    while True:
        print("\n--- Menu ---")
        print("1. Show Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        try:
            if choice == '1':
                display_books()
            elif choice == '2':
                borrow_book()
            elif choice == '3':
                return_book()
            elif choice == '4':
                print("👋 Exiting Library System. Bye!")
                logging.info("User exited the system.")
                break
            else:
                raise ValueError("Invalid menu choice.")

        except Exception as e:
            print("❌ Error:", e)
            logging.error(f"Unhandled exception: {e}")

if __name__ == "__main__":
    run_library()
