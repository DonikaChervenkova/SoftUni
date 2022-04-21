from collections import deque

duration_green = int(input())
duration_free_window = int(input())

count_passing_cars = 0
waiting_cars = deque()
car_crash = False
hit_point = ''
car = ''

command = input()
while command != "END":
    if command == "green":
        current_green_secs = duration_green
        while waiting_cars:
            if current_green_secs <= 0:
                break
            car = waiting_cars[0]
            current_car = list(waiting_cars[0])
            if current_green_secs >= len(current_car):
                current_green_secs -= len(current_car)
                count_passing_cars += 1
                waiting_cars.popleft()
                continue
            else:
                current_car = current_car[current_green_secs:]
                current_green_secs = 0
                if duration_free_window >= len(current_car):
                    count_passing_cars += 1
                    waiting_cars.popleft()
                else:
                    current_car = current_car[duration_free_window:]
                    car_crash = True
                    hit_point = current_car[0]
                    break
    else:
        waiting_cars.append(command)

    if car_crash:
        break

    command = input()

if car_crash:
    print("A crash happened!")
    print(f"{car} was hit at {hit_point}.")
else:
    print("Everyone is safe.")
    print(f"{count_passing_cars} total cars passed the crossroads.")