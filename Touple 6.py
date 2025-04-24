original_tuple = (1, 2, 3, 4)

# Step 1: Convert to list
temp_list = list(original_tuple)

# Step 2: Modify element at index 1 (value 2 → 99)
temp_list[1] = 99

# Step 3: Convert back to tuple
modified_tuple = tuple(temp_list)

print("Original tuple:", original_tuple)
print("Modified tuple:", modified_tuple)
