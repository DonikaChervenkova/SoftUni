import re

data = input()
pattern = r"((?<=^_)|(?<=\s_))[A-Za-z0-9]+\b"
# r"(^|(?<=\s))_(?P<name>[A-Za-z0-9]+)($|(?=\s)"
names = [el.group() for el in re.finditer(pattern, data)]
print(",".join(names))

