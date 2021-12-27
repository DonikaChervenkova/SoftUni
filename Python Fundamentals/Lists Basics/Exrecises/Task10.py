days = input().split("|")

energy = 100
coins = 100
bakery_is_closed = False

for current_day in days:
    current_day = current_day.split("-")

    to_do = current_day[0]
    number = int(current_day[1])

    if to_do == "rest":
        needed_energy = 100 - energy
        gained_energy = min(number, needed_energy)
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif to_do == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")

        else:
            energy += 50
            print(f"You had to rest!")
            continue

    else:
        ingredient = to_do
        coins -= number
        if coins > 0:
            print(f"You bought {ingredient}.")

        else:
            print(f"Closed! Cannot afford {ingredient}.")
            bakery_is_closed = True
            break

    if bakery_is_closed is True:
        break

if bakery_is_closed is False:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")




