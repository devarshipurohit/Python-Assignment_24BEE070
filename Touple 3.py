from datetime import date

# Define two date tuples (day, month, year)
date1_tuple = (15, 5, 2023)  # May 15, 2023
date2_tuple = (25, 12, 2023) # December 25, 2023

# Convert tuples to date objects
def tuple_to_date(dt_tuple):
    return date(dt_tuple[2], dt_tuple[1], dt_tuple[0])

date1 = tuple_to_date(date1_tuple)
date2 = tuple_to_date(date2_tuple)

# Calculate days between dates
delta = date2 - date1
days_between = abs(delta.days)  # Absolute value for difference

# Display results
print(f"First date: {date1_tuple} → {date1.strftime('%d-%b-%Y')}")
print(f"Second date: {date2_tuple} → {date2.strftime('%d-%b-%Y')}")
print(f"\nNumber of days between: {days_between} days")
