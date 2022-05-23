def func_executor(*args):
    answer = []
    for func, func_args in args:
        result = func(*func_args)
        answer.append(result)
    return answer


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2
