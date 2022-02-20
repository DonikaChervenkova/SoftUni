all_courses = {}
total_points = {}

information = input()
while information != "no more time":
    information = information.split(" -> ")
    username = information[0]
    contest = information[1]
    points = int(information[2])

    # collect info
    if contest not in all_courses:
        all_courses[contest] = {}
        all_courses[contest][username] = points
    elif contest in all_courses and username not in all_courses[contest]:
        all_courses[contest][username] = points

    # update the points if they are bigger
    if contest in all_courses and username in all_courses[contest]:
        if points > all_courses[contest][username]:
            all_courses[contest][username] = points

    information = input()

# create new dict only for name and total points
for _ in all_courses.values():
    for current_student, current_points in _.items():
        if current_student not in total_points:
            total_points[current_student] = 0
        total_points[current_student] += current_points

# sort total points
sorted_total_points = dict(sorted(total_points.items(), key=lambda x: (-x[1], x[0])))

# print
for course_name, people in all_courses.items():
    print(f"{course_name}: {len(people)} participants")
    sorted_dict = dict(sorted(all_courses[course_name].items(), key=lambda x: (-x[1], x[0])))
    counter = 1
    for name, points in sorted_dict.items():
        print(f"{counter}. {name} <::> {points}")
        counter += 1

print("Individual standings:")
counter_2 = 1
for k, v in sorted_total_points.items():
    print(f"{counter_2}. {k} -> {v}")
    counter_2 += 1