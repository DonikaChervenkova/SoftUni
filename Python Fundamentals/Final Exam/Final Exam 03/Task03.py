collection_cars = {}
n = int(input())

for _ in range(n):
    car_info = input().split("|")
    car = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])

    # collect info
    if car not in collection_cars:
        collection_cars[car] = {}
        collection_cars[car]["mileage"] = mileage
        collection_cars[car]["fuel"] = fuel

# changes
command = input()
while command != "Stop":
    command = command.split(" : ")
    to_do = command[0]
    car = command[1]

    if to_do == "Drive":
        distance = int(command[2])
        needed_fuel = int(command[3])
        if needed_fuel > collection_cars[car]['fuel']:
            print("Not enough fuel to make that ride")
        else:
            collection_cars[car]["mileage"] += distance
            collection_cars[car]["fuel"] -= needed_fuel
            print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
            if collection_cars[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del collection_cars[car]

    elif to_do == "Refuel":
        fuel_to_add = int(command[2])
        current_fuel = collection_cars[car]["fuel"]
        used_fuel_to_add = min(fuel_to_add, (75 - current_fuel))
        collection_cars[car]["fuel"] += used_fuel_to_add
        print(f"{car} refueled with {used_fuel_to_add} liters")

    elif to_do == "Revert":
        kilometers = int(command[2])
        collection_cars[car]["mileage"] -= kilometers
        if collection_cars[car]["mileage"] < 10000:
            collection_cars[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()
# sort
sorted_collection = dict(sorted(collection_cars.items(),key=lambda kvp: (-kvp[1]["mileage"],kvp[0])))

for kvp in sorted_collection.items():
    print(f"{kvp[0]} -> Mileage: {kvp[1]['mileage']} kms, Fuel in the tank: {kvp[1]['fuel']} lt.")
