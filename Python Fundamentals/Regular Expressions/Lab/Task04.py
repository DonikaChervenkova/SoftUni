import re
data = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, data)

for match in matches:
    print(match[0], end=" ")

# matches = [n.group() for num in matches]
# print(*numbers)