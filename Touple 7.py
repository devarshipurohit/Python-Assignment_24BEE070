original_tuple = (10, 20, 30, 40, 50)
index_to_remove = 2  # Remove element at index 2 (value 30)

# Slice the tuple before and after the index, then combine
new_tuple = original_tuple[:index_to_remove] + original_tuple[index_to_remove + 1:]

print("Original:", original_tuple)
print("Modified:", new_tuple)
