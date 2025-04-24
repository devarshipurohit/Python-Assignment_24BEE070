# Sample lists
list1 = [2, 7, 4, 9, 5, 2, 8]
list2 = [4, 8, 3, 10]

# Create third list using list comprehension
list3 = [num for num in list1 if num not in list2]

# Display results
print("First list:", list1)
print("Second list:", list2)
print("Elements in first list not in second:", list3)
