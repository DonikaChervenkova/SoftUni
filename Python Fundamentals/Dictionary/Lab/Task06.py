words = input().split(" ")
dictionary = {}

for current_word in words:
    current_word = current_word.lower()
    if current_word not in dictionary:
        dictionary[current_word] = 0
    dictionary[current_word] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")