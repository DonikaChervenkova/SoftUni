all_contests = {}
students_results = {}

# collect info for contests and pass for contest in all_contests
first_info = input()
while first_info != "end of contests":
    first_info = first_info.split(":")
    contest = first_info[0]
    pass_for_contest = first_info[1]

    all_contests[contest] = pass_for_contest

    first_info = input()

# collect info for correct students in students_results
second_info = input()
while second_info != "end of submissions":
    second_info = second_info.split("=>")
    student_contest = second_info[0]
    student_password = second_info[1]
    username = second_info[2]
    points = int(second_info[3])

    #check for valid contest
    if student_contest in all_contests:

        #check for valid pass of contest
        if student_password == all_contests[student_contest]:

            #save user
            if username not in students_results:
                students_results[username] = {}
                students_results[username][student_contest] = points

            elif username in students_results and student_contest not in students_results[username]:
                students_results[username][student_contest] = points

            # save bigger points
            elif username in students_results and student_contest in students_results[username]:
                if points > students_results[username][student_contest]:
                    students_results[username][student_contest] = points

    second_info = input()


# find max result and the best student name
max_name = ""
max_result = 0
for name in students_results:
    if sum(students_results[name].values()) > max_result:
        max_result = sum(students_results[name].values())
        max_name = name
#sort
sorted_all_students = dict(sorted(students_results.items(),key=lambda x: x[0]))

print(f"Best candidate is {max_name} with total {max_result} points.")
print("Ranking:")
for dictionary in sorted_all_students:
    sorted_d = dict(sorted(sorted_all_students[dictionary].items(), key=lambda x: x[1], reverse=True))
    print(dictionary)
    print('\n'.join([f"#  {k} -> {v}" for k, v in sorted_d.items()]))





