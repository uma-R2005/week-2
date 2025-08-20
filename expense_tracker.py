def expense_tracker(input_file="expenses.txt", output_file="expense_report.txt", preview_count=3):
    expenses = []
    totals = {}

    try:
        with open(input_file, "r") as file:
            lines = [line.strip() for line in file if line.strip()]

        for idx, line in enumerate(lines, 1):
            try:
                date, category, amount_str = line.split(",")
                amount = float(amount_str)
                expenses.append((date, category, amount))
                totals[category] = totals.get(category, 0) + amount
            except ValueError:
                print(f"Skipping invalid line {idx}: {line}")

        # Console preview
        print("\n=== Expense Tracker Preview ===")
        print(f"{'Date':<12} {'Category':<15} {'Amount':<10}")
        print("-" * 40)
        for exp in expenses[:preview_count]:
            print(f"{exp[0]:<12} {exp[1]:<15} ${exp[2]:<10.2f}")

        print("-" * 40)
        total_expense = sum(totals.values())
        print(f"Total Expenses: ${total_expense:.2f}\n")

        # Write detailed report
        with open(output_file, "w") as f:
            f.write("Expense Report\n")
            f.write("=" * 30 + "\n")
            for exp in expenses:
                f.write(f"{exp[0]}\t{exp[1]}\t${exp[2]:.2f}\n")

            f.write("\nCategory Totals:\n")
            for cat, total in totals.items():
                f.write(f"{cat}: ${total:.2f}\n")

            f.write(f"\nTotal Expenses: ${total_expense:.2f}\n")

        print(f"Full expense report saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Input file '{input_file}' not found.")
    except Exception as e:
        print("An error occurred:", e)


# Run the mini project
expense_tracker()
