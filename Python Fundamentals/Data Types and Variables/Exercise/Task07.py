divisor = int(input())
boundary = int(input())

for searched_n in range(boundary, 0, -1):
    if searched_n % divisor == 0:
        print(searched_n)
        break