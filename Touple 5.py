# Original list with empty tuples
original_list = [(), (1, 2), (), (3, 4), (), (5, 6, 7), ()]

# Remove empty tuples using list comprehension
cleaned_list = [tpl for tpl in original_list if tpl != ()]

# Display results
print("Original list:", original_list)
print("Cleaned list:", cleaned_list)
