banned_words = input().split(", ")
text = input()

for current_word in banned_words:
    text = text.replace(current_word, "*" * len(current_word))

print(text)