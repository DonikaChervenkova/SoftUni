journal = input().split(", ")
command = input()

while command != "Craft!":
    command = command.split(" - ")

    to_do = command[0]
    item = command[1]

    if to_do == "Collect":
        if item not in journal:
            journal.append(item)

    elif to_do == "Drop":
        if item in journal:
            journal.remove(item)

    elif to_do == "Combine Items":
        item = item.split(":")
        old_item = item[0]
        new_item = item[1]

        if old_item in journal:
            index_of_new_item = journal.index(old_item) + 1
            journal.insert(index_of_new_item, new_item)

    elif to_do == "Renew":
        if item in journal:
            x = item
            journal.remove(item)
            journal.append(x)

    command = input()

print(", ".join(journal))