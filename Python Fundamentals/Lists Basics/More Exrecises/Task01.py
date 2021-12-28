numbers = [int(i) for i in input().split(", ")]

count_zeros = numbers.count(0)

numbers_without_zeros = [i for i in numbers if i != 0]

for zero in range(count_zeros):
    numbers_without_zeros.append(0)

print(numbers_without_zeros)

