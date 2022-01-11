number = int(input())


def load_bar(num):
    percents = int(num / 10) * "%"
    dots = (10 - int(num / 10)) * "."
    loading_bar = "[" + percents + dots + "]"
    return loading_bar


if number == 100:
    print("100% Complete!")
    print(load_bar(number))
else:
    print(f"{number}% {load_bar(number)}")
    print("Still loading...")