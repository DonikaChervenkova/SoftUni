n = int(input())

registered_cars = {}

for _ in range(n):
    current_car_info = input().split(" ")
    command = current_car_info[0]
    username = current_car_info[1]

    if command == "register":
        plate_number = current_car_info[2]
        if username not in registered_cars:
            registered_cars[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered_cars[username]}")

    elif command == "unregister":
        if username not in registered_cars:
            print(f"ERROR: user {username} not found")

        else:
            print(f"{username} unregistered successfully")
            del registered_cars[username]

print("\n".join(f'{k} => {v}' for k, v in registered_cars.items()))

