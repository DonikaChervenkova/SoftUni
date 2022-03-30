import re

string = input()
total_calories = 0

pattern = r"([\|#])(?P<item>[a-zA-Z\s]+)\1(?P<date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d+)\1"
matches = re.finditer(pattern, string)

for match in matches:
    info_dict = match.groupdict()
    total_calories += int(info_dict['calories'])

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for match in re.finditer(pattern, string):
    info_dict = match.groupdict()
    print(f"Item: {info_dict['item']}, Best before: {info_dict['date']}, Nutrition: {info_dict['calories']}")
