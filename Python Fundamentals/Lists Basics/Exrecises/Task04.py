numbers = input().split(", ")
count_of_beggars = int(input())
result = []

for current_beggar in range(count_of_beggars):
    sum = 0

    beggar_numbers = numbers[current_beggar::count_of_beggars]

    for i in beggar_numbers:
        sum += int(i)

    result.append(sum)

print(result)

