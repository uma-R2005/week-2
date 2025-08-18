library = {
    "B001": {"title": "1984", "author": "George Orwell", "available": True},
    "B002": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "available": True},
    "B003": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": True}
}

borrowed_books = {}

def list_books():
    print("\nBooks in Library:")
    for book_id, info in library.items():
        status = "Available" if info["available"] else "Borrowed"
        print(f"{book_id}: {info['title']} by {info['author']} - {status}")

def borrow_book(book_id, user):
    if book_id not in library:
        return "Invalid book ID."
    if not library[book_id]["available"]:
        return "Sorry, this book is already borrowed."
    library[book_id]["available"] = False
    borrowed_books[book_id] = user
    return f"{user} borrowed '{library[book_id]['title']}' successfully."

def return_book(book_id, user):
    if book_id not in borrowed_books or borrowed_books[book_id] != user:
        return "You have not borrowed this book."
    library[book_id]["available"] = True
    del borrowed_books[book_id]
    return f"{user} returned '{library[book_id]['title']}' successfully."

def main():
    print("Library Management System")
    while True:
        print("\n1. List Books\n2. Borrow Book\n3. Return Book\n4. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            list_books()
        elif choice == "2":
            user = input("Enter your name: ").strip()
            book_id = input("Enter Book ID to borrow: ").strip().upper()
            print(borrow_book(book_id, user))
        elif choice == "3":
            user = input("Enter your name: ").strip()
            book_id = input("Enter Book ID to return: ").strip().upper()
            print(return_book(book_id, user))
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
