encrypted_message = input()
command = input()

while command != "Decode":
    command = command.split("|")
    to_do = command[0]

    if to_do == "Move":
        num_of_letters = int(command[1])   # index
        left_part = encrypted_message[:num_of_letters]
        right_part = encrypted_message[num_of_letters:]
        encrypted_message = right_part + left_part

    elif to_do == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif to_do == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {encrypted_message}")