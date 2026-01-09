def calculate_grade(average):
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 45:
        grade = "c"
    else:
        grade = "D"

marks = []
for i in range(1,6):
    mark = float(input(f"Enter marks for subject {i}:"))
    marks.append(mark)

average = sum(marks)/len(marks)
grade = calculate_grade(average)

print(f"\nAverage:{average:.2f}")
print(f"Grade:{grade}")
