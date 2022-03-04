text = input()

for idx, letter in enumerate(text):
    if letter == ":":
        print(letter + text[idx + 1])