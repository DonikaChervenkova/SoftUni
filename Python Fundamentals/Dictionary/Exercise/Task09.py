n = int(input())

all_students = {}
good_students = {}

# collect all data info
for _ in range(n):
    student_name = input()
    grade = float(input())

    all_students.setdefault(student_name, []).append(grade)

# get only good students with av_grade >= 4.50
for name, grades in all_students.items():
    average_grade_of_student = sum(grades) / len(grades)

    if average_grade_of_student >= 4.50:
        good_students[name] = average_grade_of_student

# sorting good students
sorted_good_students = dict(sorted(good_students.items(), key=lambda x: x[1], reverse=True))
print("\n".join(f"{name} -> {grade:.2f}" for name, grade in sorted_good_students.items()))
