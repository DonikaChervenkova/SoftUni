def urgent(shop_list, itm):
    shop_list.insert(0, itm)
    return shop_list


def unnecessary(shop_list, itm):
    shop_list.remove(itm)
    return shop_list


def correct(shop_list, itm, comm):
    new_item = comm.split(" ")[2]
    index_old_item = shop_list.index(itm)
    shop_list[index_old_item] = new_item
    return shop_list


def rearrange(shop_list, itm):
    shop_list.remove(itm)
    shop_list.append(itm)
    return shop_list


shopping_list = input().split("!")

command = input()

while command != "Go Shopping!":
    to_do = command.split(" ")[0]
    item = command.split(" ")[1]

    if to_do == "Urgent":
        if item not in shopping_list:
            shopping_list = urgent(shopping_list, item)

    elif to_do == "Unnecessary":
        if item in shopping_list:
            shopping_list = unnecessary(shopping_list, item)

    elif to_do == "Correct":
        if item in shopping_list:
            shopping_list = correct(shopping_list, item, command)

    elif to_do == "Rearrange":
        if item in shopping_list:
            shopping_list = rearrange(shopping_list, item)

    command = input()

print(", ".join(shopping_list))