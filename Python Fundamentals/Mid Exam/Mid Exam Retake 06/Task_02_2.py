def steal(all_loots, comm):
    count = int(comm[1])
    items_to_steal = all_loots[-count:None]
    print(", ".join(items_to_steal))
    del all_loots[-count:None]
    return all_loots


def drop(all_loots, comm):
    index = int(comm[1])
    if 0 <= index < len(all_loots):
        all_loots.append(all_loots.pop(index))
    return all_loots


def loot(all_loost,comm):
    loot_items = comm[1:]

    for current_loot in loot_items:
        if current_loot not in all_loost:
            all_loost.insert(0, current_loot)

    return all_loost


chest = input().split("|")

command = input()
while command != "Yohoho!":
    command = command.split(" ")
    to_do = command[0]

    if to_do == "Loot":
        chest = loot(chest, command)

    elif to_do == "Drop":
        chest = drop(chest, command)

    elif to_do == "Steal":
        chest = steal(chest, command)

    command = input()


if not chest:
    print("Failed treasure hunt.")
else:
    sum_all_treasures = sum([len(i) for i in chest])
    average_treasure_gain = sum_all_treasures / len(chest)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
