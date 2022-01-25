neighborhood = [int(i) for i in input().split("@")]

house_index = 0
command = input()

while command != "Love!":
    command = command.split(" ")
    steps = int(command[1])
    house_index += steps

    if 0 <= house_index < len(neighborhood):
        if neighborhood[house_index] == 0:
            print(f"Place {house_index} already had Valentine's day.")
        else:
            neighborhood[house_index] -= 2
            if neighborhood[house_index] == 0:
                print(f"Place {house_index} has Valentine's day.")

    else:
        house_index = 0
        if neighborhood[house_index] == 0:
            print(f"Place {house_index} already had Valentine's day.")
        else:
            neighborhood[house_index] -= 2
            if neighborhood[house_index] == 0:
                print(f"Place {house_index} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {house_index}.")

if len(neighborhood) == neighborhood.count(0):
    print("Mission was successful.")
else:
    non_zero_houses = len([i for i in neighborhood if i != 0])
    print(f"Cupid has failed {non_zero_houses} places.")