command = input()

count_coffee = 0
events_lower = ("coding", "dog", "cat", "movie")
events_upper = ("CODING", "DOG", "CAT", "MOVIE")

while command != "END":

    if command in events_lower:
        count_coffee += 1
    elif command in events_upper:
        count_coffee += 2

    command = input()

if count_coffee > 5:
    print("You need extra sleep")
else:
    print(count_coffee)