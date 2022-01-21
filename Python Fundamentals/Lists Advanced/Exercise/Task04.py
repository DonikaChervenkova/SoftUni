numbers = [int(i) for i in input().split(", ")]

positive_nums = ", ".join([str(i) for i in numbers if i >= 0])
negative_nums = ", ".join([str(i) for i in numbers if i < 0])
even_nums = ", ".join([str(i) for i in numbers if i % 2 == 0])
odd_nums = ", ".join([str(i) for i in numbers if i % 2 != 0])

print(f"Positive: {positive_nums}")
print(f"Negative: {negative_nums}")
print(f"Even: {even_nums}")
print(f"Odd: {odd_nums}")