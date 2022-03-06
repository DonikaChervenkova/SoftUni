import string
text = input().split()

english_alphabet = list(string.ascii_lowercase)

final_result = 0
for item in text:
    first_letter = item[0]
    number = float(item[1:-1])
    last_letter = item[-1]
    # first letter
    first_letter_position = english_alphabet.index(first_letter.lower()) + 1
    if first_letter.isupper():
        number /= first_letter_position
    elif first_letter.islower():
        number *= first_letter_position

    # last letter
    last_letter_position = english_alphabet.index(last_letter.lower()) + 1
    if last_letter.isupper():
        number -= last_letter_position
    elif last_letter.islower():
        number += last_letter_position

    final_result += number

print(f"{final_result:.2f}")
