all_names = {}
submissions = {}
results_no_banned_students = {}

# collect all info in dict all_names
information = input()
while information != "exam finished":
    information = information.split("-")
    name = information[0]

    # mark that student is banned
    if information[1] == "banned":
        if name not in all_names:
            all_names[name] = {}
        all_names[name]["banned"] = "yes"

    else:
        # collect info for language and points
        language = information[1]
        points = int(information[2])
        if name not in all_names:
            all_names[name] = {}
        all_names[name].setdefault("language", []).append(language)
        all_names[name].setdefault("points", []).append(points)

        # collect info for submissions
        submissions.setdefault(language, []).append(name)

    information = input()

# create dict only for NO banned students with there MAX points
for name in all_names:
    if "banned" not in all_names[name]:
        if name not in results_no_banned_students:
            results_no_banned_students[name] = max(all_names[name]["points"])
# sort
sorted_no_banned_students = dict(sorted(results_no_banned_students.items(),key=lambda x: (-x[1], x[0])))
sorted_submissions = dict(sorted(submissions.items(), key=lambda x: (-len(x[1]), x[0])))

print("Results:")
print('\n'.join([f"{name} | {result}" for name, result in sorted_no_banned_students.items()]))
print("Submissions:")
print('\n'.join([f"{key} - {len(value)}" for key, value in sorted_submissions.items()]))