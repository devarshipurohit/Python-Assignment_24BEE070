# Get input from user
string = input("Enter a string: ")

# Define vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# Count vowels (case-insensitive)
count = 0
for char in string.lower():
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")
