n = int(input())
special_sums = (5, 7, 11)

for current_number in range(1, n + 1):
    sum_digits = 0

    for digit in str(current_number):
        sum_digits += int(digit)

    if sum_digits in special_sums:
        print(f"{current_number} -> True")
    else:
        print(f"{current_number} -> False")


