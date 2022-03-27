stops = input()

command = input()
while command != "Travel":
    command = command.split(":")
    to_do = command[0]

    if to_do == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]
            print(stops)

    elif to_do == "Remove Stop":
        start_idx = int(command[1])
        end_idx = int(command[2])
        if start_idx >= 0 and end_idx < len(stops):
            stops = stops[:start_idx] + stops[end_idx + 1:]
        print(stops)

    elif to_do == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")