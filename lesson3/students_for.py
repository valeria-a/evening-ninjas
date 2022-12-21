students = ["Nadav", "Gal", "Barel"]
grades = [[100, 99], [99, 99], [98, 99, 100]]

for i in range(len(students)):
    student_name = students[i]
    student_grades = grades[i]
    grades_sum = 0
    for g in student_grades:
        grades_sum += g
    avg = grades_sum / len(student_grades)
    print(f"{student_name}: {student_grades}, avg:{avg}")
