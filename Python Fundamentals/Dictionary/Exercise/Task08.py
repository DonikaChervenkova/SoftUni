courses = {}

line = input()
while line != "end":
    course_info = line.split(" : ")
    type_course = course_info[0]
    student_name = course_info[1]

    courses.setdefault(type_course, []).append(student_name)

    line = input()

sorted_courses = dict(sorted(courses.items(), key=lambda x: (-len(x[1]))))

for current_course in sorted_courses:
    print(f"{current_course}: {len(sorted_courses[current_course])}")
    print("\n".join(f'-- {name}' for name in sorted(sorted_courses[current_course])))


