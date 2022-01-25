all_items = input().split(", ")

command = input()

while command != "Craft!":
    command = command.split(" - ")
    to_do = command[0]

    if to_do == "Collect":
        item = command[1]
        if item not in all_items:
            all_items.append(item)

    elif to_do == "Drop":
        item = command[1]
        if item in all_items:
            all_items.remove(item)

    elif to_do == "Combine Items":
        sub_command = command[1].split(":")
        old_item = sub_command[0]
        new_item = sub_command[1]

        if old_item in all_items:
            index_of_old_item = all_items.index(old_item)
            all_items.insert(index_of_old_item + 1, new_item)

    elif to_do == "Renew":
        item = command[1]
        if item in all_items:
            all_items.remove(item)
            all_items.append(item)

    command = input()

print(", ".join(all_items))