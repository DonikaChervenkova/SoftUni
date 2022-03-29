import re
from functools import reduce

data = input()

# emojis
pattern_emojis = r"([\:|\*])\1([A-Z][a-z]{2,})\1\1"
emojis = re.finditer(pattern_emojis, data)

count_emojis = len([i.group(0) for i in emojis])
all_valid_emojis = [i.group(0) for i in re.finditer(pattern_emojis, data)]

# numbers
pattern_numbers = r"(\d)"
numbers = re.finditer(pattern_numbers, data)
cool_threshold = reduce((lambda x, y: x * y), [int(i) for i in ([i.group(1) for i in numbers])])

# print
print(f"Cool threshold: {cool_threshold}")
print(f"{count_emojis} emojis found in the text. The cool ones are:")
for emoji in all_valid_emojis:
    emoji_letters = emoji[2:-2]
    coolness_of_emoji = 0

    for letter in emoji_letters:
        coolness_of_emoji += ord(letter)
    if coolness_of_emoji > cool_threshold:
        print(emoji)
