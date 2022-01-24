targets = [int(i) for i in input().split(" ")]


def check_index(tgs, idx):
    if 0 <= idx < len(tgs):
        return True
    else:
        return False


def check_start_end_index(tgs, start_idx, end_idx):
    if start_idx >= 0 and end_idx < len(tgs):
        return True


def do_shoot(tgs, idx, p):
    if check_index(tgs, idx):
        tgs[idx] -= p
        if tgs[idx] <= 0:
            tgs.pop(idx)


def do_add(tgs, idx, v):
    if check_index(tgs, idx):
        tgs.insert(idx, v)
    else:
        print("Invalid placement!")


def do_strike(tgs, idx, r):
    start_idx = idx - r
    end_idx = idx + r

    if check_start_end_index(tgs, start_idx, end_idx):
        del tgs[start_idx:end_idx + 1]
    else:
        print("Strike missed!")


command = input()

while command != "End":
    command = command.split(" ")
    to_do = command[0]
    index = int(command[1])

    if to_do == "Shoot":
        power = int(command[2])
        do_shoot(targets, index, power)

    elif to_do == "Add":
        value = int(command[2])
        do_add(targets, index, value)

    elif to_do == "Strike":
        radius = int(command[2])
        do_strike(targets, index, radius)

    command = input()


print("|".join([str(i) for i in targets]))