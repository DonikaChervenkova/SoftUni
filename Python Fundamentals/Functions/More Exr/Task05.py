num1 = int(input())
num2 = int(input())
num3 = int(input())


def multiplication_sign(number1, number2, number3):
    result = number1 * number2 * number3
    if result < 0:
        return "negative"
    elif result == 0:
        return "zero"
    elif result >= 1:
        return "positive"


print(multiplication_sign(num1, num2, num3))
