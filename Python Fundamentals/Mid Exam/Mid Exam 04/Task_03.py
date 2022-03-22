houses = [int(i) for i in input().split("@")]

command = input()
house_index = 0

while command != "Love!":
    command = command.split(" ")
    number = int(command[1])

    house_index += number

    if house_index < len(houses):
        if houses[house_index] == 0:
            print(f"Place {house_index} already had Valentine's day.")
        else:
            houses[house_index] -= 2
            if houses[house_index] == 0:
                print(f"Place {house_index} has Valentine's day.")

    else:
        house_index = 0
        if houses[house_index] == 0:
            print(f"Place {house_index} already had Valentine's day.")
        else:
            houses[house_index] -= 2
            if houses[house_index] == 0:
                print(f"Place {house_index} has Valentine's day.")

    command = input()


print(f"Cupid's last position was {house_index}.")

if houses.count(0) == len(houses):
    print("Mission was successful.")
else:
    houses_non_zero = [i for i in houses if i != 0]
    count_houses_non_zero = len(houses_non_zero)
    print(f"Cupid has failed {count_houses_non_zero} places.")