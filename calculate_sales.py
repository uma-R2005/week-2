import csv

sales_file = 'sales.csv'
total_revenue = 0

with open(sales_file, newline='') as file:
    reader = csv.DictReader(file)
    print("Total Sales per Product:")
    for row in reader:
        units = int(row['units_sold'])
        price = float(row['unit_price'])
        total_sales = units * price
        total_revenue += total_sales
        print(f"- {row['product_name']}: ${total_sales:.2f}")

print(f"\nOverall Total Revenue: ${total_revenue:.2f}")
