numbers = list(map(int, input().split(" ")))
n = int(input())

sorted_numbers = sorted(numbers, reverse=True)
nums_to_stay = sorted_numbers[:-n]
answer = list(filter(lambda x: x in nums_to_stay, numbers))
print(", ".join([str(num) for num in answer]))


