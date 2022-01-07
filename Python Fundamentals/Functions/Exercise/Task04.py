number = input()


def odd_and_even_sum(num):
    sum_odd = 0
    sum_even = 0
    digits = [int(i) for i in number]
    for digit in digits:
        if digit % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit

    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


print(odd_and_even_sum(number))