numbers = [float(i) for i in input().split()]


def absolute_values(nums):
    abs_nums = [abs(i) for i in nums]
    return abs_nums


print(absolute_values(numbers))
