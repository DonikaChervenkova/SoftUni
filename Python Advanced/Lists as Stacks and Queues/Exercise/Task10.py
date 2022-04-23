from collections import deque

cups = deque([int(i) for i in input().split()])
filled_bottles = [int(i) for i in input().split()]

wasted_water = 0
while True:
    if cups and filled_bottles:

        if filled_bottles[-1] >= cups[0]:
            wasted_water += (filled_bottles[-1] - cups[0])
            filled_bottles.pop()
            cups.popleft()
        else:
            need_more_water_for_a_cup = True
            while True:
                cups[0] -= filled_bottles[-1]
                filled_bottles.pop()
                if cups[0] <= 0:
                    wasted_water += abs(cups[0])
                    need_more_water_for_a_cup = False
                    cups.popleft()
                    break

                if not filled_bottles:
                    break
            if not filled_bottles and need_more_water_for_a_cup:
                break
    else:
        break

if not cups:
    print(f"Bottles: {' '.join([str(i) for i in filled_bottles])}")
else:
    print(f"Cups: {' '.join([str(i) for i in cups])}")
print(f"Wasted litters of water: {wasted_water}")