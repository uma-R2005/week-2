import requests
import xml.etree.ElementTree as ET

def get_rates():
    url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'
    response = requests.get(url)
    root = ET.fromstring(response.content)

    namespaces = {'gesmes': 'http://www.gesmes.org/xml/2002-08-01',
                  'def': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref'}

    # find Cube elements with currency rates
    rates = {'EUR': 1.0}  # Base currency is Euro
    for cube in root.findall('.//def:Cube[@currency]', namespaces):
        currency = cube.attrib['currency']
        rate = float(cube.attrib['rate'])
        rates[currency] = rate

    return rates

def convert(amount, from_currency, to_currency, rates):
    if from_currency != 'EUR':
        amount = amount / rates[from_currency]  # convert to EUR first
    return amount * rates[to_currency]

rates = get_rates()

amount = float(input("Enter amount: "))
from_curr = input("From currency (e.g., USD): ").upper()
to_curr = input("To currency (e.g., INR): ").upper()

if from_curr in rates and to_curr in rates:
    converted = convert(amount, from_curr, to_curr, rates)
    print(f"{amount} {from_curr} = {converted:.2f} {to_curr}")
else:
    print("Currency not supported.")
