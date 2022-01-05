nums = [float(i) for i in input().split(" ")]


def rounding(numbers):
    round_nums = [round(i) for i in numbers]
    return round_nums


print(rounding(nums))