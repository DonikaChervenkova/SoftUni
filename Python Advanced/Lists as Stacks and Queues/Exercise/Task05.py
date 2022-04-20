from collections import deque

queue = deque()

n = int(input())

for _ in range(n):
    pump = [int(i) for i in input().split()]
    queue.append(pump)

for idx in range(n):
    car_fuel = 0
    completed = True
    for petrol, distance in queue:
        car_fuel += petrol
        if distance > car_fuel:
            completed = False
            break
        car_fuel -= distance
    if completed:
        print(idx)
        break
    queue.append(queue.popleft())
