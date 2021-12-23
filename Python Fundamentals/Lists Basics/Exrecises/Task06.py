numbers = [int(i) for i in input().split(" ")]
n = int(input())

sorted_numbers = sorted(numbers)
nums_to_stay = sorted_numbers[n:]

answer = [str(i) for i in numbers if i in nums_to_stay]
print(", ".join(answer))