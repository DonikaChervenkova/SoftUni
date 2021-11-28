word = input()

list_of_double_char = []

for current_char in word:
    list_of_double_char.append(current_char * 2)

print("".join(list_of_double_char))
