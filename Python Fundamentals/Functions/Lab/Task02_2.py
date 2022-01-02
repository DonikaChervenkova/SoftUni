def numbers(list):
    num = [abs(float(x)) for x in list]
    return num

print(numbers(input().split(" ")))