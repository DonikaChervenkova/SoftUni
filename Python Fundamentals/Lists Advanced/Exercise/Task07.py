numbers = [int(i) for i in input().split(", ")]

max_num = max(numbers)
max_group = (max_num // 10) * 10
if max_num % 10 != 0:
    max_group += 10

for current_group in range(10, max_group + 1, 10):

    start = current_group - 9
    end = current_group
    nums_in_group = [i for i in numbers if i in range(start, end + 1)]

    print(f"Group of {current_group}'s: {nums_in_group}")
