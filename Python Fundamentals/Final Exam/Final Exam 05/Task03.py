collection = {}

info = input()
while info != "Sail":
    info = info.split("||")
    town = info[0]
    population = int(info[1])
    gold = int(info[2])

    # collect data in dict
    if town not in collection:
        collection[town] = {}
        collection[town]['population'] = 0
        collection[town]['gold'] = 0
    collection[town]['population'] += population
    collection[town]['gold'] += gold

    info = input()

# changes
command = input()
while command != "End":
    command = command.split("=>")
    to_do = command[0]
    town = command[1]

    if to_do == "Plunder":
        people = int(command[2])
        stolen_gold = int(command[3])
        collection[town]['population'] -= people
        collection[town]['gold'] -= stolen_gold
        print(f"{town} plundered! {stolen_gold} gold stolen, {people} citizens killed.")
        if collection[town]['population'] <= 0 or collection[town]['gold'] <= 0:
            del collection[town]
            print(f"{town} has been wiped off the map!")

    elif to_do == "Prosper":
        gold = int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            collection[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {collection[town]['gold']} gold.")

    command = input()

# sort
sorted_collection = dict(sorted(collection.items(),key=lambda kvp: (-kvp[1]['gold'], kvp[0])))
if not collection:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(collection)} wealthy settlements to go to:")
    for kvp in sorted_collection.items():
        print(f"{kvp[0]} -> Population: {kvp[1]['population']} citizens, Gold: {kvp[1]['gold']} kg")