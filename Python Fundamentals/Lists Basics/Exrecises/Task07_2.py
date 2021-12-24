def out_of_stock(gifts_all, current_gift):
    gifts_all = [i if i != current_gift else "None" for i in gifts_all]
    return gifts_all


def required(gifts_all, current_gift, idx):
    gifts_all[idx] = current_gift


def just_in_case(gifts_all, current_gift):
    gifts_all[-1] = current_gift


all_gifts = input().split(" ")

command = input()
while command != "No Money":
    command = command.split(" ")
    to_do = command[0]
    gift = command[1]

    if to_do == "OutOfStock":
        if gift in all_gifts:
            all_gifts = out_of_stock(all_gifts, gift)

    elif to_do == "Required":
        index = int(command[2])
        if 0 <= index < len(all_gifts):
            required(all_gifts, gift, index)

    elif to_do == "JustInCase":
        just_in_case(all_gifts, gift)

    command = input()

print(" ".join(filter(lambda x: x != "None", all_gifts)))

