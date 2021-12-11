word1 = input()
word2 = input()

new_word = ""
prev_word = ""

for i in range(0, len(word1) + 1):
    new_word = word2[:i + 1] + word1[i + 1:]

    if new_word != word1 and new_word != prev_word:
        print(new_word)

        prev_word = new_word
        new_word = ""

