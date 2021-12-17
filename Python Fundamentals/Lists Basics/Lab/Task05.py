n = int(input())
numbers = []
filtered_nums = []

for current_number in range(n):
    number = int(input())
    numbers.append(number)

command = input()

if command == "even":
    filtered_nums = [i for i in numbers if i % 2 == 0]

elif command == "odd":
    filtered_nums = [i for i in numbers if i % 2 != 0]

elif command == "negative":
    filtered_nums = [i for i in numbers if i < 0]

elif command == "positive":
    filtered_nums = [i for i in numbers if i >= 0]

print(filtered_nums)