def add(stps, comm):
    index = int(comm.split(":")[1])
    string = comm.split(":")[2]
    if 0 <= index < len(stps):
        return stps[:index] + string + stps[index:]
    else:
        return stps


def remove(stps, comm):
    start_idx = int(command.split(":")[1])
    end_idx = int(command.split(":")[2])
    if start_idx >= 0 and end_idx < len(stps):
        return stps[:start_idx] + stps[end_idx + 1:]
    else:
        return stps


def switch(stps, comm):
    old_string = command.split(":")[1]
    new_string = command.split(":")[2]
    if old_string in stps:
        return stps.replace(old_string, new_string)
    else:
        return stps


stops = input()

command = input()
while command != "Travel":
    to_do = command.split(":")[0]

    if to_do == "Add Stop":
        stops = add(stops, command)
        print(stops)

    elif to_do == "Remove Stop":
        stops = remove(stops, command)
        print(stops)

    elif to_do == "Switch":
        stops = switch(stops, command)
        print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")