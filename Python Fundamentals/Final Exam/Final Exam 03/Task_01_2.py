message = list(input())

command = input()

while command != "Reveal":
    command = command.split(":|:")
    to_do = command[0]

    if to_do == "InsertSpace":
        index = int(command[1])
        message.insert(index, " ")
        print("".join(message))

    elif to_do == "Reverse":
        substring = command[1]
        messages_as_str = "".join(message)

        if substring in messages_as_str:
            messages_as_str = messages_as_str.replace(substring, "", 1)
            messages_as_str += substring[::-1]
            print(messages_as_str)
            message = list(messages_as_str)

        else:
            print("error")

    elif to_do == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        messages_as_str = "".join(message)

        if substring in messages_as_str:
            messages_as_str = messages_as_str.replace(substring, replacement)
            print(messages_as_str)
            message = list(messages_as_str)

    command = input()

answer = "".join(message)
print(f"You have a new text message: {answer}")