animals = input().split(", ")

if animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")

else:
    for index, animal in enumerate(animals):
        if animal == "wolf":
            position_of_wolf = index + 1
            position_sheep = len(animals) - position_of_wolf
            print(f"Oi! Sheep number {position_sheep}! You are about to be eaten by a wolf!")
