number = int(input())


def load_bar(num):
    loading_bar = []
    count_percent = int(num / 10)
    count_dots = 10 - count_percent

    for percent in range(count_percent):
        loading_bar.append("%")

    for dot in range(count_dots):
        loading_bar.append(".")

    loading_bar = "".join(loading_bar)

    if number == 100:
        print("100% Complete!")
        print(f"[{loading_bar}]")
    else:
        print(f"{number}% [{loading_bar}]")
        print("Still loading...")


load_bar(number)