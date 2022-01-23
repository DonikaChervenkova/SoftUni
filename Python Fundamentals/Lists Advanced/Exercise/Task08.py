Ttext = input().split(" ")
new_text = []

for current_word in text:
    digits = []
    alphas = []
    new_word = []

    for letter in current_word:
        if letter.isdigit():
            digits.append(letter)
        else:
            alphas.append(letter)

    first_letter = chr(int("".join(digits)))

    new_word.append(first_letter)
    new_word += alphas

    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    new_word = "".join(new_word)
    new_text.append(new_word)

print(" ".join(new_text))


