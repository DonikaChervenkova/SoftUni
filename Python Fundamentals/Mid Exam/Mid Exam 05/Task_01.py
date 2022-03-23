students = int(input())
total_count_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_attendaces = 0

for current_student in range(1, students + 1):
    attendances = int(input())

    total_bonus = attendances / total_count_lectures * (5 + additional_bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendaces = attendances

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_attendaces} lectures.")