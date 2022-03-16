import re
from itertools import islice

all_players = {}
players = input().split(", ")

for current_player in players:
    if current_player not in all_players:
        all_players[current_player] = {}
        all_players[current_player]['distance'] = 0

info = input()
while info != "end of race":
    pattern_name = r"[A-Za-z]+"
    name = ''.join(re.findall(pattern_name, info))

    pattern_distance = r"[0-9]"
    numbers = re.findall(pattern_distance, info)
    distance = sum([int(i) for i in numbers])

    if name in all_players:
        all_players[name]['distance'] += distance

    info = input()

sorted_players = dict(sorted(all_players.items(), key=lambda kvp: -kvp[1]['distance']))

winners = list(islice(sorted_players, 3))
print(f"""1st place: {winners[0]}
2nd place: {winners[1]}
3rd place: {winners[2]}""")