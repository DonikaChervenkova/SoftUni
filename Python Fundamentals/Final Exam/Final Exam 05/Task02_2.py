import re

data = input()
pattern_emojis = r"(\:\:|\*\*)([A-Z][a-z]{2,})\1"
emojis = [e.group(0) for e in re.finditer(pattern_emojis, data)]

pattern_numbers = r"\d"
numbers = [int(num.group(0)) for num in re.finditer(pattern_numbers, data)]

cool_threshold = 1
for num in numbers:
    cool_threshold *= num

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for current_emoji in emojis:
    current_emoji_letters = current_emoji[2:-2]
    coolness_of_emoji = sum([ord(letter) for letter in current_emoji_letters])
    if coolness_of_emoji > cool_threshold:
        print(current_emoji)

