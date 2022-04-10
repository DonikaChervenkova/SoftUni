from collections import deque

quantity = int(input())
people = deque()

command = input()
while command != "Start":
    people.append(command)
    command = input()

more_commands = input()
while more_commands != "End":
    more_commands = more_commands.split()
    if more_commands[0] == "refill":
        more_water = int(more_commands[1])
        quantity += more_water
    else:
        wanted_litters = int(more_commands[0])
        if wanted_litters <= quantity:
            quantity -= wanted_litters
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")

    more_commands = input()

print(f"{quantity} liters left")