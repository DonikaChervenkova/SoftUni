import re

pattern = r"www\.[A-Za-z0-9\-]+\.[a-z]+((\.[a-z]+)?)+"
all_data = []
data = input()
while data:
    all_data.append(data)
    matches = re.finditer(pattern, data)
    for match in matches:
        print(match.group(0))
    data = input()


