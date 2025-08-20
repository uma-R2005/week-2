import csv

total_delay = 0
delayed_flights = 0
total_flights = 0

with open('flights.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        delay = int(row['delay_minutes'])
        total_flights += 1
        if delay > 0:
            delayed_flights += 1
            total_delay += delay

# Calculate average delay
if delayed_flights > 0:
    average_delay = total_delay / delayed_flights
else:
    average_delay = 0

print(f"Total flights: {total_flights}")
print(f"Delayed flights: {delayed_flights}")
print(f"Average delay (in minutes): {average_delay:.2f}")
