def do_move(comm, encr_mssg):
    num_of_letters = int(comm[1])  # index
    left_part = encr_mssg[:num_of_letters]
    right_part = encr_mssg[num_of_letters:]
    return right_part + left_part


def do_insert(comm, encr_mssg):
    index = int(comm[1])
    value = comm[2]
    return encr_mssg[:index] + value + encr_mssg[index:]


def do_changeall(comm, encr_mssg):
    substring = comm[1]
    replacement = comm[2]
    return encr_mssg.replace(substring, replacement)


encrypted_message = input()
command = input()

while command != "Decode":
    command = command.split("|")
    to_do = command[0]

    if to_do == "Move":
        encrypted_message = do_move(command, encrypted_message)

    elif to_do == "Insert":
        encrypted_message = do_insert(command, encrypted_message)

    elif to_do == "ChangeAll":
        encrypted_message = do_changeall(command, encrypted_message)

    command = input()

print(f"The decrypted message is: {encrypted_message}")
