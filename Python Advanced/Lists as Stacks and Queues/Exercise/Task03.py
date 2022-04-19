from collections import deque

food = int(input())
orders = deque([int(i) for i in input().split()])

print(max(orders))

while orders:
    if orders[0] <= food:
        food -= orders.popleft()
    else:
        break

if orders:
    print(f"Orders left: {' '.join([str(i) for i in orders])}")
else:
    print("Orders complete")
