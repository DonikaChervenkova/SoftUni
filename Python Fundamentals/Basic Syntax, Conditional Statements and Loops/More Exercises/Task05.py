string = input().lower()
searched_words = ("Sand", "Water", "Fish", "Sun")

counter = 0

for current_word in searched_words:

    if current_word.lower() in string:
        count_per_word = string.count(current_word.lower())
        counter += count_per_word

print(counter)