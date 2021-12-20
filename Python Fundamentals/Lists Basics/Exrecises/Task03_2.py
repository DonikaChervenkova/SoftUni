cards = input().split(" ")

team_a_out = []
team_b_out = []
game_over = False

for current_card in cards:
    team = current_card.split("-")[0]
    player_number = int(current_card.split("-")[1])

    if team == "A":
        if player_number not in team_a_out:
            team_a_out.append(player_number)
            if len(team_a_out) >= 5:
                game_over = True
                break

    elif team == "B":
        if player_number not in team_b_out:
            team_b_out.append(player_number)
            if len(team_b_out) >= 5:
                game_over = True
                break

print(f"Team A - {11 - len(team_a_out)}; Team B - {11 - len(team_b_out)}")
if game_over:
    print("Game was terminated")
