number_1 = int(input())
number_2 = int(input())
number_3 = int(input())


def smallest_num(num_1, num_2, num_3):
    smallest_number = min(num_1, num_2, num_3)
    return smallest_number


print(smallest_num(number_1, number_2, number_3))