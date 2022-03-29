text = input()

command = input()
while command != "Generate":
    command = command.split(">>>")
    to_do = command[0]

    if to_do == "Contains":
        substring = command[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")

    elif to_do == "Flip":
        type = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        new_part_of_txt = text[start_index:end_index]

        if type == "Upper":
            new_part_of_txt = new_part_of_txt.upper()
        elif type == "Lower":
            new_part_of_txt = new_part_of_txt.lower()

        text = text[:start_index] + new_part_of_txt + text[end_index:]
        print(text)

    elif to_do == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        text = text[:start_index] + text[end_index:]
        print(text)

    command = input()

print(f"Your activation key is: {text}")