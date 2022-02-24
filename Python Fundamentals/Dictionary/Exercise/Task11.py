book = {}
all_users = {}

command = input()
# collect all data
while command != "Lumpawaroo":
    if "|" in command:
        command = command.split(" | ")
        side = command[0]
        user = command[1]

        # add new users
        if user not in all_users:
            all_users[user] = side

    elif "->" in command:
        command = command.split(" -> ")
        user = command[0]
        side = command[1]

        # add new users
        if user not in all_users:
            all_users[user] = side
        # change the side os user
        else:
            all_users[user] = side

        print(f"{user} joins the {side} side!")

    command = input()

# collect data by side in new dict
for user, side in all_users.items():
    book.setdefault(side, []).append(user)

# sort
sorted_book = dict(sorted(book.items(), key=lambda x: (-len(x[1]), x[0])))

for key, value in sorted_book.items():
    print(f"Side: {key}, Members: {len(value)}")
    print('\n'.join([f"! {i}" for i in sorted(value)]))

