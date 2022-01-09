numbers = [int(i) for i in input().split(" ")]


def min_of_nums(nums):
    return f"The minimum number is {min(nums)}"


def max_of_nums(nums):
    return f"The maximum number is {max(nums)}"


def sum_of_nums(nums):
    return f"The sum number is: {sum(nums)}"


print(min_of_nums(numbers))
print(max_of_nums(numbers))
print(sum_of_nums(numbers))