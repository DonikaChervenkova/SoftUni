initial_energy = int(input())

count_wins = 0
game_over = False
command = input()

while command != "End of battle":
    distance = int(command)

    if initial_energy >= distance:
        initial_energy -= distance
        count_wins += 1
        if count_wins % 3 == 0:
            initial_energy += count_wins

    else:
        game_over = True
        print(f"Not enough energy! Game ends with {count_wins} won battles and {initial_energy} energy")
        break

    command = input()

if not game_over:
    print(f"Won battles: {count_wins}. Energy left: {initial_energy}")