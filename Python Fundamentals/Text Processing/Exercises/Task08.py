text = input().split()

total_sum = 0
for item in text:
    left_alpha = item[0]
    right_alpha = item[-1]
    number = int(item[1:-1])

    if left_alpha.isupper():
        position = ord(left_alpha) - 64
        number /= position

    elif left_alpha.islower():
        position = ord(left_alpha) - 96
        number *= position

    if right_alpha.isupper():
        position = ord(right_alpha) - 64
        number -= position

    elif right_alpha.islower():
        position = ord(right_alpha) - 96
        number += position

    total_sum += number

print(f"{total_sum:.2f}")

