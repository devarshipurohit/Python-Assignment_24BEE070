original_set = {"Dev", "Banney", "Ram", "Yug", "Anshul", "Krish"}

# Split into A and B sets
a_names = {name for name in original_set if name.startswith('A')}
b_names = {name for name in original_set if name.startswith('B')}

print("Original set:", original_set)
print("Names starting with A:", a_names)
print("Names starting with B:", b_names)
