import re

string = input()
pattern = r"([\/|\=])([A-Z][A-Za-z]{2,})\1"
matches = re.finditer(pattern, string)
print(f"Destinations: {', '.join([m.group(2) for m in matches])}")
print(f"Travel Points: {sum([len(m.group(2)) for m in re.finditer(pattern, string)])}")