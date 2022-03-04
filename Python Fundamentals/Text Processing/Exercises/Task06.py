text = input()
new_text = ""

for idx, letter in enumerate(text):
    # all idx except "zero idx"
    if 1 <= idx < len(text):
        if text[idx] != text[idx - 1]:
            new_text += letter
    # "zero idx"
    elif idx == 0:
        new_text += letter

print(new_text)