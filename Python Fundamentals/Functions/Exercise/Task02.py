number_1 = int(input())
number_2 = int(input())
number_3 = int(input())


def sum_numbers(a, b):
    result = a + b
    return result


def subtract(sum_of_nums, c):
    result = sum_of_nums - c
    return result


def add_and_subtract(num_1, num_2, num_3):
    sum = sum_numbers(num_1, num_2)
    answer = subtract(sum, num_3)
    return answer


print(add_and_subtract(number_1, number_2, number_3))
