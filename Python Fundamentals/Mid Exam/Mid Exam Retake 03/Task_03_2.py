def shoot(trgs, idx, v):
    trgs[idx] -= v
    if trgs[idx] <= 0:
        trgs.pop(idx)
    return trgs


def add(trgs, idx, v):
    trgs.insert(idx, v)
    return trgs


def strike(trgs, start_idx, end_idx):
        del trgs[start_idx: end_idx + 1]
        return trgs


targets = [int(i) for i in input().split(" ")]

command = input()

while command != "End":
    command = command.split(" ")
    to_do = command[0]
    index = int(command[1])
    value = int(command[2])

    if to_do == "Shoot":
        if 0 <= index < len(targets):
            targets = shoot(targets, index, value)

    elif to_do == "Add":
        if 0 <= index < len(targets):
            targets = add(targets, index, value)
        else:
            print("Invalid placement!")

    elif to_do == "Strike":
        start_index = index - value
        end_index = index + value
        if start_index >= 0 and end_index < len(targets):
            targets = strike(targets, start_index, end_index)
        else:
            print("Strike missed!")

    command = input()

print("|".join([str(i) for i in targets]))