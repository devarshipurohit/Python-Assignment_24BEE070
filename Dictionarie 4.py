input_str = input("Enter a string: ")
frequency = {}

for char in input_str:
    frequency[char] = frequency.get(char, 0) + 1

print("Character frequencies:", frequency)
