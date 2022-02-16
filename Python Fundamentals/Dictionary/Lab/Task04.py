all_students = {}

command = input()
while command[0].isupper():
    student_info = command.split(":")
    key = student_info[2]
    value = student_info[0] + " - " + student_info[1]
    all_students.setdefault(key, []).append(value)

    command = input()

searched_course = command.replace("_", " ")


print("\n".join(all_students[searched_course]))
