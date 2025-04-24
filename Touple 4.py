# Create a list of food-price tuples
food_items = [
    ("Pizza", 129.99),
    ("Burger", 100),
    ("Salad", 70),
    ("Coffee", 50),
    ("Ice Cream", 100)
]

# Sort by price in descending order
sorted_items = sorted(food_items, key=lambda x: x[1], reverse=True)

# Display results
print("Food items sorted by price (highest to lowest):")
for item in sorted_items:
    print(f"• {item[0]:<10} - Rs{item[1]:.2f}")
