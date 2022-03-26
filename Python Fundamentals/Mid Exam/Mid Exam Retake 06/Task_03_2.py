def repair(pirateship, idx, h, max_h):
    pirateship[idx] += h
    if pirateship[idx] > max_h:
        pirateship[idx] = max_h
    return pirateship


def defend(pirateship, start_idx, end_idx, dmge):
    for idx in range(start_idx, end_idx + 1):
        pirateship[idx] -= dmge
        if pirateship[idx] <= 0:
            print(f"You lost! The pirate ship has sunken.")
            return False
    return pirateship


def fire(war_ship, idx, comm):
    damage = int(comm[2])
    war_ship[idx] -= damage
    if war_ship[idx] <= 0:
        print("You won! The enemy ship has sunken.")
        return False
    else:
        return war_ship


pirate_ship = [int(i) for i in input().split(">")]
warship = [int(i) for i in input().split(">")]
max_health = int(input())

command = input()
game_over = False

while command != "Retire":
    command = command.split(" ")
    to_do = command[0]

    if to_do == "Fire":
        index = int(command[1])
        if 0 <= index < len(warship):

            if fire(warship, index, command):
                pass
            else:
                game_over = True
                break

    elif to_do == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if start_index >= 0 and end_index < len(pirate_ship):
            if not defend(pirate_ship, start_index, end_index, damage):
                game_over = True
                break

    elif to_do == "Repair":
        index = int(command[1])
        health = int(command[2])

        if 0 <= index < len(pirate_ship):
            pirate_ship = repair(pirate_ship, index, health, max_health)

    elif to_do == "Status":
        count_lowers = len(list(filter(lambda x: x < (max_health * 0.2), pirate_ship)))

        print(f"{count_lowers} sections need repair.")

    command = input()


if not game_over:
    pirate_sum = sum(pirate_ship)
    warship_sum = sum(warship)
    print(f"Pirate ship status: {pirate_sum}")
    print(f"Warship status: {warship_sum}")