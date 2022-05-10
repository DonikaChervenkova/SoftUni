import os

command = input()
while command != "End":
    command = command.split("-")
    to_do = command[0]
    file_name = command[1]

    if to_do == "Create":
        file = open(file_name, "w")
        file.close()

    elif to_do == "Add":
        content = command[2]
        with open(file_name, "a") as file:
            file.write(f'{content}\n')

    elif to_do == "Replace":
        old_str = command[2]
        new_str = command[3]
        try:
            new_lines = []
            with open(file_name, "r") as file:
                all_lines = file.read().split("\n")
                for line in all_lines:
                    if line != "":
                        line = line.replace(old_str, new_str)
                        new_lines.append(line)

            file = open(file_name, "w")
            file.close()

            with open(file_name, "a") as file:
                for line in new_lines:
                    file.write(f"{line}\n")

        except FileNotFoundError:
            print("An error occurred")

    elif to_do == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")

    command = input()