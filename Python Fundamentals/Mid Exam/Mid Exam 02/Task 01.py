efficiency_1 = int(input())
efficiency_2 = int(input())
efficiency_3 = int(input())
students = int(input())

total_efficiency = efficiency_1 + efficiency_2 + efficiency_3
working_hours = 0

while students > 0:
    working_hours += 1

    if working_hours % 4 == 0:
        pass

    else:
        students -= total_efficiency

print(f"Time needed: {working_hours}h.")
