chest = input().split("|")

sum_of_treasures_len = 0
command = input()

while command != "Yohoho!":
    command = command.split(" ")
    to_do = command[0]

    if to_do == "Loot":
        items_to_loot = command[1:]
        for item in items_to_loot:
            if item not in chest:
                chest.insert(0, item)

    elif to_do == "Drop":
        index = int(command[1])
        if 0 <= index < len(chest):
            item = chest[index]
            chest.pop(index)
            chest.append(item)

    elif to_do == "Steal":
        count = int(command[1])
        items_to_steal = chest[-count:None]
        print(", ".join(items_to_steal))
        del chest[-count:None]

    command = input()


if not chest:
    print("Failed treasure hunt.")
else:
    for item in chest:
        sum_of_treasures_len += len(item)

    average_gain = sum_of_treasures_len / len(chest)

    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")