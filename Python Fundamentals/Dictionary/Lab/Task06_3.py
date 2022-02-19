from collections import Counter
words = [i.lower() for i in input().split(" ")]

dictionary = Counter(words)


for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")