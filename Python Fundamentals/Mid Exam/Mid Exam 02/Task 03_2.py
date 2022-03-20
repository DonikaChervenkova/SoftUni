numbers = list(map(int, input().split(" ")))

average_number = sum(numbers) / len(numbers)
greater_than_avr = [i for i in numbers if i > average_number]
greater_than_avr.sort(reverse=True)

if not greater_than_avr:
    print("No")
else:
    print(" ".join(str(i) for i in greater_than_avr[:5]))