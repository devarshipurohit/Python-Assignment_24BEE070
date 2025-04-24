# Sample list containing boys' names (as tuples) and girls' names (as strings)
names_list = [("Devarshi",), "Riya", ("Raj",),("Ram",), "Sophia", ("Lakshay",), ("Amolik",), "Yashvi"]

# Count boys and girls
boys = sum(1 for element in names_list if isinstance(element, tuple))
girls = len(names_list) - boys  # Total elements minus boys

# Display results
print("List contents:", names_list)
print(f"Number of boys: {boys}")
print(f"Number of girls: {girls}")
