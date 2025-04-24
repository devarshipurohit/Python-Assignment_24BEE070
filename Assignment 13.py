import csv

students_list = []

# Read the CSV file
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        roll_no = row['Roll No']
        name = row['Name']
        marks_str = row['Marks']
        
        # Parse marks (e.g., "Physics-74/100; Maths-80/100; Electrical-76/100")
        subjects_marks = {}
        total = 0
        for entry in marks_str.split('; '):
            subject, score = entry.split('-')
            obtained_marks = int(score.split('/')[0].strip())  # Extract numerator (e.g., 74)
            subjects_marks[subject.strip()] = obtained_marks
            total += obtained_marks
        
        # Build the student dictionary
        student_data = {
            "Roll No": roll_no,
            "Name": name,
            **subjects_marks,
            "Total": total
        }
        students_list.append(student_data)

# Display the result
for student in students_list:
    print(student)
