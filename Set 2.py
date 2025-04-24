import random

# Generate 10 unique random numbers between 15 and 45
number_set = set(random.sample(range(15, 46), 10))

# Count numbers < 30
count_less_30 = sum(1 for num in number_set if num < 30)

# Remove numbers > 35
filtered_set = {num for num in number_set if num <= 35}

print("Original set:", number_set)
print(f"Numbers < 30: {count_less_30}")
print("Filtered set (≤35):", filtered_set)
