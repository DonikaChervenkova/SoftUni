all_plants = {}
filtered_info = {}
n = int(input())

for _ in range(n):
    info = input().split("<->")
    plant = info[0]
    rarity = int(info[1])

    # collect info in dict
    if plant not in all_plants:
        all_plants[plant] = {}
        all_plants[plant] = {"rarity": rarity,
                            "rating": []}

# do changes
command = input()
while command != "Exhibition":
    command = command.split(": ")
    to_do = command[0]
    part_2_info = command[1].split(" - ")

    if to_do == "Rate":
        plant = part_2_info[0]
        rating = int(part_2_info[1])
        if plant in all_plants:
            all_plants[plant]["rating"].append(rating)
        else:
            print("error")

    elif to_do == "Update":
        plant = part_2_info[0]
        new_rarity = int(part_2_info[1])
        if plant in all_plants:
            all_plants[plant]["rarity"] = new_rarity
        else:
            print("error")

    elif to_do == "Reset":
        plant = part_2_info[0]
        if plant in all_plants:
            all_plants[plant]["rating"].clear()
        else:
            print("error")

    else:
        print("error")

    command = input()

# add "avg_rating" for each plant
for current_plant in all_plants.keys():
    all_rating_as_list = all_plants[current_plant]["rating"]
    if not all_rating_as_list:
        avg_rating = 0.00
    else:
        avg_rating = sum(all_rating_as_list) / len(all_rating_as_list)

    all_plants[current_plant]["avg_rating"] = avg_rating


# create filtered_info = {plant: [rarity,avg_rating]}
for name in all_plants.keys():
    current_rarity = all_plants[name]["rarity"]
    current_avg_rating = all_plants[name]["avg_rating"]
    filtered_info[name] = [current_rarity, current_avg_rating]

# sort
sorted_filtered_info = dict(sorted(filtered_info.items(),key= lambda x: (x[1][0], x[1][1]), reverse=True))

print("Plants for the exhibition:")
for plant, v in sorted_filtered_info.items():
    print(f"- {plant}; Rarity: {v[0]}; Rating: {v[1]:.2f}")



