words = [i.lower() for i in input().split(" ")]
dictionary = {}

for current_word in words:
    dictionary[current_word] = words.count(current_word)

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")