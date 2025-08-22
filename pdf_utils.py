from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

def generate_invoice(filename, customer_name, items):
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER

    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 50, "Invoice")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Customer: {customer_name}")

    c.drawString(50, height - 130, "Items:")

    y = height - 160
    total = 0
    for item, price in items.items():
        c.drawString(70, y, f"{item}: ${price:.2f}")
        total += price
        y -= 20

    c.drawString(50, y - 20, f"Total: ${total:.2f}")

    c.save()
    print(f"Invoice saved as {filename}")
