numbers = [int(i) for i in input().split()]

reversed_numbers = []

while numbers:
    reversed_numbers.append(numbers.pop())

print(' '.join([str(i) for i in reversed_numbers]))