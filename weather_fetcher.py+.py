from forex_python.converter import CurrencyRates

# Create an instance of the currency converter
c = CurrencyRates()

# Input values
amount = float(input("Enter amount: "))
from_currency = input("From currency (e.g., USD): ").upper()
to_currency = input("To currency (e.g., INR): ").upper()

# Convert
converted_amount = c.convert(from_currency, to_currency, amount)

# Output
print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
