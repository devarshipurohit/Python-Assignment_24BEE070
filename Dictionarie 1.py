# Create three dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'a': 10}  # 'a' key will overwrite dict1's 'a'

# Concatenate dictionaries (last dict's keys take precedence)
merged_dict = {**dict1, **dict2, **dict3}

print("Merged Dictionary:", merged_dict)
