rooms = input().split("|")

health = 100
bitcoins = 0
reached_rooms = 0
game_over = False

for current_room in rooms:
    current_room = current_room.split(" ")

    command = current_room[0]

    if command == "potion":
        amount = int(current_room[1])

        reached_rooms += 1
        needed_health = 100 - health
        used_health = min(amount, needed_health)
        health += used_health
        if health > 100:
            health = 100

        print(f"You healed for {used_health} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        amount = int(current_room[1])

        reached_rooms += 1
        bitcoins += amount
        print(f"You found {amount} bitcoins.")

    else:
        monster = command
        attack = int(current_room[1])

        reached_rooms += 1
        health -= attack

        if health > 0:
            print(f"You slayed {monster}.")

        else:
            game_over = True
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {reached_rooms}")
            break

    if game_over:
        break

if not game_over:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")








