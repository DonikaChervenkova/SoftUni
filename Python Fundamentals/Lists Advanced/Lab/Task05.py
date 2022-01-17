numbers = [int(i) for i in input().split(", ")]

indexes_of_even_numbers = []

for index, num in enumerate(numbers):
    if num % 2 == 0:
        indexes_of_even_numbers.append(index)

print(indexes_of_even_numbers)
