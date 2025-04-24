# Sample data: {employee_roll: {"dept": dept_no, "salary": salary}}
employees = {
    101: {"dept": 1, "salary": 50000},
    102: {"dept": 1, "salary": 60000},
    103: {"dept": 2, "salary": 45000},
    104: {"dept": 2, "salary": 55000},
    105: {"dept": 2, "salary": 40000}
}

dept_salaries = {}

# Group salaries by department
for emp in employees.values():
    dept = emp["dept"]
    salary = emp["salary"]
    dept_salaries.setdefault(dept, []).append(salary)

# Calculate min and max per department
for dept, salaries in dept_salaries.items():
    print(f"Dept {dept}: Min = {min(salaries)}, Max = {max(salaries)}")
