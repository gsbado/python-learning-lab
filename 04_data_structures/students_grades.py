students = [("Carlos", 20, 9.2), ("Miguel", 22, 7.5), ("Manuela", 19, 8.1), ("Gabriela", 23, 9.9),("Cleodir", 20, 7.3)]

sum_grades = 0
best_student = students[0]

for name, age, grade in students:
    sum_grades += grade

    if grade > best_student[2]:
        best_student = (name, age, grade)

average = sum_grades / len(students)

print("=== STUDENTS LIST ===")
for name, age, grade in students:
    print(f"Name: {name} | Age: {age} years | Grade: {grade}")
print(f"The class average this semester is: {average:.1f}")
print(f"The student with the highest grade is: {best_student[0]} with a grade of {best_student[2]:.1f}")