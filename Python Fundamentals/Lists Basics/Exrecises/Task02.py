factor = int(input())
count = int(input())

numbers = [(num * factor) for num in range(1, count + 1)]

print(numbers)