import random

# Generate 20 random integers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(20)]
print("Generated list of random numbers:")
print(random_numbers)

# Get user input
try:
    target = int(input("\nEnter a number to search in the list: "))
except ValueError:
    print("Please enter a valid integer!")
    exit()

# Find all occurrences
positions = [i for i, num in enumerate(random_numbers) if num == target]

# Display results
if positions:
    print(f"\nNumber {target} found at position(s):")
    for pos in positions:
        print(f"• Index {pos} (value: {random_numbers[pos]})")
else:
    print(f"\nNumber {target} is not present in the list.")
