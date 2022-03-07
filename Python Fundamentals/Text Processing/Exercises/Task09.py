text = input()
result = ""
numbers = []
text_without_nums = ""

index = 0
while index < len(text):
    if text[index].isdigit():
        if (index + 1) < len(text) and text[index + 1].isdigit():
            digit = int(text[index] + text[index + 1])
            index += 2
        else:
            digit = int(text[index])
            index += 1

        numbers.append(digit)
        text_without_nums += " "
    else:
        text_without_nums += text[index]
        index += 1

text_without_nums = text_without_nums.split()

for idx in range(len(numbers)):
    item = text_without_nums[idx].upper() * numbers[idx]
    result += item

unique_symbols = len(set(list(result)))
print(f"Unique symbols used: {unique_symbols}")
print(result)