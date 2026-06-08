grades = []
grade = 0.0

while grade >= 0.0 and grade <= 10.0:
  grade = float(input("Enter a grade between 0 and 10 (or a negative number to stop): "))
  grades.append(grade)
  if grade < 0.0 or grade > 10.0:
    grades.remove(grade)
    break
  else:
    continue

works = len(grades)
total_grades = sum(grades)
average_grades = total_grades / works

print(f"You have delivered {works} works in this semester.")
print(f"Your grades from this semester are: {grades}")
print(f"Your sum of grades is: {total_grades:.2f}")
print(f"Your average grade is: {average_grades:.2f}")