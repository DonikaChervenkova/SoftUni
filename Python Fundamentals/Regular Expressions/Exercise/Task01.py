import re

all_data = []
data = input()
while data:
    all_data.append(data)
    data = input()

pattern = r"\d+"
for current_item in all_data:
    matches = re.findall(pattern, current_item)
    if matches:
        print(' '.join(matches), end=" ")

