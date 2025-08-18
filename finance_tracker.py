import json
import os

finance_data = {}

def load_data(filename="finance_data.json"):
    global finance_data
    if os.path.exists(filename):
        with open(filename, "r") as f:
            finance_data = json.load(f)
        print("Data loaded.")
    else:
        finance_data = {
            "2025-08": {
                "income": 3000,
                "expenses": {"food": 250, "transport": 120}
            },
            "2025-09": {
                "income": 3200,
                "expenses": {"food": 300, "entertainment": 90}
            }
        }
        print("No previous data found. Sample data loaded.")

def save_data(filename="finance_data.json"):
    with open(filename, "w") as f:
        json.dump(finance_data, f, indent=4)
    print("Data saved.")

def add_transaction(date, category, amount, transaction_type="expense"):
    if date not in finance_data:
        finance_data[date] = {"income": 0, "expenses": {}}
    if transaction_type == "income":
        finance_data[date]["income"] += amount
    else:
        if not category:
            print("Category required for expense.")
            return
        finance_data[date]["expenses"][category] = finance_data[date]["expenses"].get(category, 0) + amount

def monthly_summary(date):
    if date not in finance_data:
        return f"No data for {date}"
    income = finance_data[date]["income"]
    expenses = finance_data[date]["expenses"]
    total_expenses = sum(expenses.values())
    balance = income - total_expenses
    summary = f"\nSummary for {date}:\n"
    summary += f" Income: ${income:.2f}\n"
    summary += " Expenses:\n"
    for cat, amt in expenses.items():
        summary += f"  - {cat}: ${amt:.2f}\n"
    summary += f" Total Expenses: ${total_expenses:.2f}\n"
    summary += f" Balance: ${balance:.2f}\n"
    return summary

def total_expenses_by_category():
    totals = {}
    for month in finance_data.values():
        for cat, amt in month["expenses"].items():
            totals[cat] = totals.get(cat, 0) + amt
    return totals

def main():
    load_data()
    print("Welcome to Personal Finance Tracker")
    
    while True:
        print("\nOptions:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Monthly Summary")
        print("4. View Total Expenses by Category")
        print("5. Save and Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            date = input("Enter date (YYYY-MM): ")
            try:
                amount = float(input("Enter income amount: "))
                add_transaction(date, None, amount, "income")
                print("Income added.")
            except ValueError:
                print("Invalid amount.")

        elif choice == "2":
            date = input("Enter date (YYYY-MM): ")
            category = input("Enter expense category: ")
            try:
                amount = float(input("Enter expense amount: "))
                add_transaction(date, category, amount, "expense")
                print("Expense added.")
            except ValueError:
                print("Invalid amount.")

        elif choice == "3":
            date = input("Enter month to view summary (YYYY-MM): ")
            print(monthly_summary(date))

        elif choice == "4":
            totals = total_expenses_by_category()
            if not totals:
                print("No expense data available.")
            else:
                print("\nTotal expenses by category:")
                for cat, amt in totals.items():
                    print(f" - {cat}: ${amt:.2f}")

        elif choice == "5":
            save_data()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
