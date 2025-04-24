import random

# Generate 5 random odd integers between 1 and 19
odd_numbers = [random.randrange(1, 20, 2) for _ in range(5)]
print("Original list of odd integers:", odd_numbers)

# Generate 4 random even integers between 0 and 18
even_numbers = [random.randrange(0, 20, 2) for _ in range(4)]
print("List of even integers:", even_numbers)

# Replace third element (index 2) with even numbers list
odd_numbers[2] = even_numbers
print("\nAfter replacing third element with even list:", odd_numbers)

# Flatten the nested list
flattened = []
for item in odd_numbers:
    if isinstance(item, list):
        flattened.extend(item)
    else:
        flattened.append(item)
print("Flattened list:", flattened)

# Sort the final list
sorted_list = sorted(flattened)
print("\nFinal sorted list:", sorted_list)
