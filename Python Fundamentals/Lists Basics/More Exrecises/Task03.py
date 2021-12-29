numbers = input().split(" ")
string = list(input())

message = []
indexes = []

for current_number in numbers:
    sum_of_digits = 0

    for digit in current_number:
        sum_of_digits += int(digit)

    indexes.append(sum_of_digits)

for current_index in indexes:
    if 0 <= current_index < len(string):
        message.append(string[current_index])
        string.pop(current_index)

    else:
        current_index = current_index - ((current_index // len(string)) * len(string))
        message.append(string[current_index])
        string.pop(current_index)


print("".join(message))






