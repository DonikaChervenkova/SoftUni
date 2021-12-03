all_animals = input().split(", ")

all_animals.reverse()

if all_animals[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(all_animals)):
        if all_animals[i] == "wolf":
            print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")											
