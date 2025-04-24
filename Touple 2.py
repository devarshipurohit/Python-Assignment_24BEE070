# List of student tuples (roll_no, name, age)
students = [
    (101, 'Rahul', 20),
    (102, 'Priya', 21),
    (103, 'Amit', 19),
    (104, 'Sneha', 22),
    (105, 'Kiran', 20)
]

# Create separate lists using list comprehension
roll_numbers = [student[0] for student in students]
names = [student[1] for student in students]
ages = [student[2] for student in students]

# Display results
print("Original student list:")
print(students)
print("\nRoll Numbers:", roll_numbers)
print("Names:", names)
print("Ages:", ages)
