phonebook = {}

command = input()
while command[0].isupper():
    contact_info = command.split("-")
    name = contact_info[0]
    phone_number = contact_info[1]
    phonebook[name] = phone_number

    command = input()

n = int(command)

for search in range(1, n + 1):
    searched_name = input()
    if phonebook.get(searched_name):
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")