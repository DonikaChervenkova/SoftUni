first_line = input().split(", ")
words = input().split(", ")

substrings = []

for searched_substring in first_line:
    for current_word in words:
        if searched_substring in current_word:
            if searched_substring not in substrings:
                substrings.append(searched_substring)

print(substrings)
