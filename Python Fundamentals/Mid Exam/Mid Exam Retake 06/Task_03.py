pirate_ship = [int(i) for i in input().split('>')]
warship = [int(i) for i in input().split('>')]
max_health = int(input())

pirates_won = False
warship_won = False

command = input()
while command != "Retire":
    command = command.split(" ")
    to_do = command[0]

    if to_do == "Fire":
        index = int(command[1])
        damage = int(command[2])

        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                pirates_won = True
                break
        if pirates_won is True:
            break

    if pirates_won is True:
        break

    elif to_do == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])

        if start_index >= 0 and end_index < len(pirate_ship):

            for index, section in enumerate(pirate_ship):
                if index in range(start_index, end_index + 1):
                    pirate_ship[index] -= damage

                    if pirate_ship[index] <= 0:
                        print("You lost! The pirate ship has sunken.")
                        warship_won = True
                        break
                if warship_won is True:
                    break
            if warship_won:
                break
        if warship_won:
            break
    if warship_won:
        break

    elif to_do == "Repair":
        index = int(command[1])
        health = int(command[2])

        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health

    elif to_do == "Status":
        count_lowers = len(list(filter(lambda x: x < (max_health * 0.2), pirate_ship)))

        #for section in pirate_ship:
            #if section < (max_health_capacity * 0.2):
                #count_lowers += 1
        print(f"{count_lowers} sections need repair.")

    command = input()

if pirates_won is False and warship_won is False:
    pirate_sum = sum(pirate_ship)
    warship_sum = sum(warship)
    print(f"Pirate ship status: {pirate_sum}")
    print(f"Warship status: {warship_sum}")
