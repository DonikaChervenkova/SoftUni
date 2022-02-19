count_words = int(input())

dictionary = {}
for number_of_word in range(count_words):
    word = input()
    synonym = input()
    dictionary.setdefault(word, []).append(synonym)

for key, value in dictionary.items():
    print(key + " - " + ', '.join(value))