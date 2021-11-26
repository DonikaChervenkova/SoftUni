word = str(input())

word_as_list = list(word)
word_as_list.reverse()
reversed_word = "".join(word_as_list)
print(reversed_word)