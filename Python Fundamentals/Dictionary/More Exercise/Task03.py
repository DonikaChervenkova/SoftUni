all_players = {}

data = input()
while data != "Season end":
    if "->" in data:
        data = data.split(" -> ")
        player = data[0]
        position = data[1]
        skill = int(data[2])

        # collect info
        if player not in all_players:
            all_players[player] = {}
        if position not in all_players[player]:
            all_players[player][position] = skill
        # update with bigger value
        if skill > all_players[player][position]:
            all_players[player][position] = skill

    else:
        player_1, player_2 = data.split(" vs ")
        if (player_1 in all_players) and (player_2 in all_players):
            positions_player_1 = set(i for i in all_players[player_1].keys())
            positions_player_2 = set(i for i in all_players[player_2].keys())
            common_positions = list(positions_player_1 & positions_player_2)
            if common_positions:
                # check total points of common positions
                total_common_points_p1 = sum([all_players[player_1][pos] for pos in common_positions])
                total_common_points_p2 = sum([all_players[player_2][pos] for pos in common_positions])
                # duel
                if total_common_points_p1 != total_common_points_p2:
                    total_points_p1 = sum(all_players[player_1].values())
                    total_points_p2 = sum(all_players[player_2].values())
                    if total_points_p1 > total_points_p2:
                        del all_players[player_2]
                    elif total_points_p2 > total_points_p1:
                        del all_players[player_1]

    data = input()

dict_of_total_points = {}
# add total points in dict
for player in all_players:
    total_points_of_player = sum(all_players[player].values())
    dict_of_total_points[player] = total_points_of_player

sorted_total_points = dict(sorted(dict_of_total_points.items(), key=lambda kvp: (-kvp[1], kvp[0])))

for name, t_points in sorted_total_points.items():
    print(f"{name}: {t_points} skill")
    sorted_skills = dict(sorted(all_players[name].items(), key=lambda kvp: (-kvp[1], kvp[0])))
    for current_position, current_skill in sorted_skills.items():
        print(f"- {current_position} <::> {current_skill}")

