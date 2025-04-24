names = set()

# Add 5 names
names.update(["Devarshi", "Rahul", "Yash", "Rahi", "Anshul"])
print("Initial set:", names)

# Modify "Bob" → "Bobby"
if "Bob" in names:
    names.remove("Anshul")
    names.add("Krish")
print("After modification:", names)

# Delete 2 names
names.discard("Rahi")
names.discard("Yug")
print("Final set:", names)
