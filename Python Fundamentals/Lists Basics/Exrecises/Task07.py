all_gifts = input().split(" ")

command = input()

while command != "No Money":
    command = command.split(" ")
    to_do = command[0]
    gift = command[1]

    if to_do == "OutOfStock":
        for i, item in enumerate(all_gifts):
            if item == gift:
                all_gifts[i] = "None"

    elif to_do == "Required":
        index = int(command[2])

        if 0 <= index < (len(all_gifts)):
            all_gifts[index] = gift

    elif to_do == "JustInCase":
        all_gifts[-1] = gift

    command = input()

new_gifts = " ".join([i for i in all_gifts if i != "None"])
print(new_gifts)
