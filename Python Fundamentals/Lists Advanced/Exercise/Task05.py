rooms = int(input())

total_free_chairs = 0
not_enough_chairs = False

for current_room_number in range(1, rooms + 1):
    room = input().split(" ")
    chairs_count = len(room[0])
    people = int(room[1])

    if people > chairs_count:
        not_enough_chairs = True
        needed_chairs_in_room = people - chairs_count
        print(f"{needed_chairs_in_room} more chairs needed in room {current_room_number}")
    elif people < chairs_count:
        free_chairs_in_room = chairs_count - people
        total_free_chairs += free_chairs_in_room

if not not_enough_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")

