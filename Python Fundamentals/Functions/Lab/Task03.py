operator = input()
num_one = int(input())
num_two = int(input())


def multiply_nums(x, y):
    result = x * y
    return result


def divide_nums(x, y):
    if y != 0:
        result = int(x / y)
        return result


def add_nums(x, y):
    result = x + y
    return result


def subtract_nums(x, y):
    result = x - y
    return result


all_commands = {
    "multiply": multiply_nums,
    "divide": divide_nums,
    "add": add_nums,
    "subtract": subtract_nums
}

print(all_commands[operator](num_one, num_two))


