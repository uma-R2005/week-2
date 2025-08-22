from pdf_utils import generate_invoice

def main():
    print("Welcome to the Invoice Generator!")
    
    customer = input("Enter customer name: ")
    items = {}
    
    print("Enter items and prices. Type 'done' when finished.")
    while True:
        item = input("Item name: ")
        if item.lower() == 'done':
            break
        try:
            price = float(input("Price: "))
        except ValueError:
            print("Invalid price, try again.")
            continue
        items[item] = price

    filename = f"invoice_{customer.replace(' ', '_')}.pdf"
    generate_invoice(filename, customer, items)

if __name__ == "__main__":
    main()
