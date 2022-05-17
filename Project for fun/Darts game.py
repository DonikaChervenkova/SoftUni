player_1, player_2 = input().split(", ")
total_points_1 = 501
total_points_2 = 501

game_over = False
first_won = False
second_won = False

dartboard = []
for _ in range(7):
    line = [int(el) if el not in ("D", "T", "B") else el for el in input().split()]
    dartboard.append(line)

player_turn = 0
coordinates = input()
while coordinates:
    player_turn += 1
    coordinates = coordinates[1:-1].split(", ")
    row = int(coordinates[0])
    column = int(coordinates[1])

    current_score = 0
    if 0 <= row < 7 and 0 <= column < 7:
        if dartboard[row][column] not in ("D", "T", "B"):
            current_score = dartboard[row][column]
        elif dartboard[row][column] == "B":
            game_over = True
        elif dartboard[row][column] == "D":
            current_score = (dartboard[0][column] + dartboard[6][column] + dartboard[row][0] + dartboard[row][6]) * 2
        elif dartboard[row][column] == "T":
            current_score = (dartboard[0][column] + dartboard[6][column] + dartboard[row][0] + dartboard[row][6]) * 3

    # turn of player 1
    if player_turn % 2 != 0:
        if game_over:
            first_won = True
        else:
            total_points_1 -= current_score
            if total_points_1 <= 0:
                game_over = True
                first_won = True
    # turn of player 2
    else:
        if game_over:
            second_won = True
        else:
            total_points_2 -= current_score
            if total_points_2 <= 0:
                game_over = True
                second_won = True
    if game_over:
        break

    coordinates = input()

total_moves = player_turn // 2
if player_turn % 2 != 0:
    total_moves += 1

if first_won:
    print(f"{player_1} won the game with {total_moves} throws!")
elif second_won:
    print(f"{player_2} won the game with {total_moves} throws!")
