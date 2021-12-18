numbers = [int(i) for i in input().split(" ")]

opposite_numbers = []

for current_num in numbers:
    if current_num >= 0:
        opposite_numbers.append(-current_num)

    elif current_num < 0:
        opposite_numbers.append(abs(current_num))

print(opposite_numbers)