prices = {"apple": 1.5, "bread": 2.0, "milk": 3.5}
quantities = {"apple": 3, "bread": 2, "milk": 1}

total = 0
for item in prices:
    if item in quantities:
        total += prices[item] * quantities[item]

print(f"Total bill: Rs{total:.2f}")  # Output: Total bill: Rs12.0
