from collections import deque

bullet_price = int(input())
size_of_barrel = int(input())
bullets = [int(i) for i in input().split()]
locks = deque([int(i) for i in input().split()])
intelligence = int(input())

count_shoots = 0
while locks:
    if not bullets:
        break

    count_shoots += 1
    intelligence -= bullet_price

    # destroy lock
    if bullets[-1] <= locks[0]:
        print("Bang!")
        locks.popleft()
        bullets.pop()
    # not destroyed lock
    else:
        print("Ping!")
        bullets.pop()

    if count_shoots == size_of_barrel:
        count_shoots = 0
        if bullets:
            print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence}")