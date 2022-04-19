clothes = [int(i) for i in input().split()]
capacity = int(input())

count_racks = 0

current_rack = 0
while True:
    if clothes:
        while True:
            clothing = clothes.pop()
            current_rack += clothing
            if current_rack > capacity:
                count_racks += 1
                current_rack = clothing
                break
            elif current_rack == capacity:
                count_racks += 1
                current_rack = 0
            if not clothes:
                break
    else:
        break

if current_rack > 0:
    count_racks += 1

print(count_racks)