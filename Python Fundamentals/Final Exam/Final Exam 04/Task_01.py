password = input()

command = input()

while command != "Done":
    command = command.split(" ")
    to_do = command[0]

    if to_do == "TakeOdd":
        password = password[1::2]
        print(password)

    elif to_do == "Cut":
        index = int(command[1])
        lenght = int(command[2])
        end_index = index + lenght
        password = password[:index] + password[end_index:]
        print(password)

    elif to_do == "Substitute":
        substr = command[1]
        substitute = command[2]
        if substr in password:
            password = password.replace(substr, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")