n = int(input())

destroyed_ships = 0
field = []

for current_row in range(n):
    row = [int(i) for i in input().split(" ")]
    field.append(row)

all_attacks = input().split(" ")

for current_attack in all_attacks:
    current_attack = [int(i) for i in current_attack.split("-")]
    attacked_point = field[current_attack[0]][current_attack[1]]

    if attacked_point != 0:
        field[current_attack[0]][current_attack[1]] -= 1
        if field[current_attack[0]][current_attack[1]] == 0:
            destroyed_ships += 1

print(destroyed_ships)

