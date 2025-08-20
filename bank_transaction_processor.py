def process_transactions(input_file, output_file, preview_count=4):
    balance = 0
    statement_lines = []

    try:
        with open(input_file, "r") as file:
            lines = [line.strip() for line in file if line.strip()]

        total_transactions = len(lines)

        print("\n=== Bank Transaction Statement (Preview) ===")
        print(f"{'Type':<10} {'Amount':<10} {'Balance After':<15}")
        print("-" * 40)

        for i, line in enumerate(lines):
            transaction_type, amount_str = line.split(",")
            amount = float(amount_str)

            if transaction_type.upper() == "DEPOSIT":
                balance += amount
                message = f"Deposited: ${amount:.2f}"
            elif transaction_type.upper() == "WITHDRAW":
                balance -= amount
                message = f"Withdrew: ${amount:.2f}"
            else:
                message = f"Unknown transaction: {line}"

            statement_lines.append(message)

            # Print only first preview_count transactions
            if i < preview_count:
                print(f"{transaction_type.capitalize():<10} ${amount:<9.2f} ${balance:<14.2f}")

        # No message about remaining transactions on console

        final_balance_msg = f"\nFinal Balance: ${balance:.2f}"
        statement_lines.append(final_balance_msg)
        print("-" * 40)
        print(final_balance_msg)

        with open(output_file, "w") as file:
            for line in statement_lines:
                file.write(line + "\n")

        print(f"\nFull statement saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Input file '{input_file}' not found.")
    except Exception as e:
        print("An error occurred:", e)


# Run the function
process_transactions("transactions.txt", "statement.txt")
