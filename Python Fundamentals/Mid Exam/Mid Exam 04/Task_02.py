all_products = input().split("!")

command = input()

while command != "Go Shopping!":
    command = command.split(" ")
    to_do = command[0]

    if to_do == "Urgent":
        item = command[1]
        if item not in all_products:
            all_products.insert(0, item)

    elif to_do == "Unnecessary":
        item = command[1]
        if item in all_products:
            all_products.remove(item)

    elif to_do == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in all_products:
            index_of_old_item = all_products.index(old_item)
            all_products[index_of_old_item] = new_item

    if to_do == "Rearrange":
        item = command[1]
        if item in all_products:
            x = item
            all_products.remove(item)
            all_products.append(x)

    command = input()

print(", ".join(all_products))
