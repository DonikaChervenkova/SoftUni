numbers = [int(i) for i in input().split(" ")]
average_number = sum(numbers) / len(numbers)

nums_over_than_avr = [i for i in numbers if i > average_number]
if not nums_over_than_avr:
    print("No")
else:
    nums_over_than_avr.sort(reverse=True)
    result = nums_over_than_avr[:5]
    print(" ".join([str(i) for i in result]))