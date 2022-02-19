from collections import Counter
words = [i.lower() for i in input().split(" ")]

dictionary = Counter(words)

filtered_words = list(filter(lambda item: item[1] % 2 != 0, dictionary.items()))
print(" ".join([item[0] for item in filtered_words]))