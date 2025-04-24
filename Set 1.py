# Program to convert list of words to uppercase set
words = ["apple", "Banana", "cherry", "apple", "dragonfruit"]
uppercase_set = {word.upper() for word in words}

print("Original list:", words)
print("Uppercase set:", uppercase_set)
