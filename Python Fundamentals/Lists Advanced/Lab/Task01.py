text = list(input())

vowels_lower = ['a', 'o', 'u', 'e', 'i']
vowels_upper = [i.upper() for i in vowels_lower]

new_text = []

for letter in text:
    if letter not in vowels_lower:
        if letter not in vowels_upper:
            new_text.append(letter)

print("".join(new_text))
