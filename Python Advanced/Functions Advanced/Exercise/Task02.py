def ood_or_even(current_command, nums):
    result = 0
    sum_nums = []

    if current_command == 'Odd':
        sum_nums = sum([num for num in nums if num % 2 != 0])
    elif current_command == 'Even':
        sum_nums = sum([num for num in nums if num % 2 == 0])
    result = sum_nums * len(nums)
    return result


command = input()
numbers = [int(i) for i in input().split()]

print(ood_or_even(command, numbers))