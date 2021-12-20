all_red_cards = input().split(" ")

team_a = 11
team_b = 11
given_red_cards_a_team = []
given_red_cards_b_team = []
game_over = False

for current_red_card in all_red_cards:
    current_red_card = current_red_card.split("-")
    team = current_red_card[0]
    player = int(current_red_card[1])

    if team == "A":
        if player not in given_red_cards_a_team:
            given_red_cards_a_team.append(player)
            team_a -= 1

    elif team == "B":
        if player not in given_red_cards_b_team:
            given_red_cards_b_team.append(player)
            team_b -= 1

    if team_a < 7 or team_b < 7:
        game_over = True
        break

print(f"Team A - {team_a}; Team B - {team_b}")

if game_over is True:
    print("Game was terminated")
