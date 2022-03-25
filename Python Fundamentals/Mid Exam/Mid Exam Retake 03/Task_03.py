targets = [int(i) for i in input().split(" ")]

command = input()

while command != "End":
    command = command.split(" ")
    to_do = command[0]
    index = int(command[1])

    if to_do == "Shoot":
        if 0 <= index < len(targets):
            power = int(command[2])
            targets[index] -= power

            if targets[index] <= 0:
                targets.pop(index)

    elif to_do == "Add":
        if 0 <= index < len(targets):
            value = int(command[2])
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif to_do == "Strike":
        radius = int(command[2])
        start = index - radius
        end = index + radius

        if start >= 0 and end < len(targets):
            del targets[start: end + 1]
        else:
            print("Strike missed!")

    command = input()

targets_of_str = [str(i) for i in targets]
print("|".join(targets_of_str))