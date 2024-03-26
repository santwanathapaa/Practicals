"""CP-1404 - Prac-03
Capitalist Conrad wants a stock price simulator for a volatile stock."""

import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_price_simulation.txt"

price = INITIAL_PRICE
number_of_days = 0

# Open the file for writing
out_file = open(OUTPUT_FILE, 'w')

print(f"Starting price: ${price:,.2f}")

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0

    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    number_of_days += 1

    # Print to console
    print(f"On day {number_of_days} price is: ${price:,.2f}")

    # Print to file
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file
out_file.close()