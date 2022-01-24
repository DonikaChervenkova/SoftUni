targets = [int(i) for i in input().split(" ")]

command = input()

while command != "End":
    command = command.split(" ")
    to_do = command[0]
    index = int(command[1])

    if to_do == "Shoot":
        power = int(command[2])

        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif to_do == "Add":
        value = int(command[2])

        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif to_do == "Strike":
        radius = int(command[2])
        start_index = index - radius
        end_index = index + radius

        if start_index >= 0 and end_index < len(targets):
            del targets[start_index:end_index + 1]
        else:
            print("Strike missed!")

    command = input()


print("|".join([str(i) for i in targets]))