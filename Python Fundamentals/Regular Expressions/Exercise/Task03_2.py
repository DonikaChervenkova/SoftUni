import re

data = input()
searched_word = input()
pattern = fr"(?i)\b{searched_word}\b"
matches = re.finditer(pattern, data)
print(len([m.group(0) for m in matches]))
