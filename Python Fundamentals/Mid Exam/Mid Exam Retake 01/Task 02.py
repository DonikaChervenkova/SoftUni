all_people = int(input())
cabins = [int(i) for i in input().split(" ")]

no_more_free_space = False
no_more_waiting_people = False

for index, current_cabin in enumerate(cabins):

    free_seats_in_cabin = 4 - current_cabin
    waiting_people_per_cabin = min(all_people, 4)
    entered_people = min(waiting_people_per_cabin, free_seats_in_cabin)

    all_people -= entered_people
    cabins[index] = current_cabin + entered_people

# if No more waiting people and  still have a free space
if all_people == 0 and (len(cabins) * 4) > sum(cabins):
    print("The lift has empty spots!")
    print(" ".join([str(i) for i in cabins]))

# if there ARE still waiting people and No more free space
elif all_people > 0 and cabins.count(4) == len(cabins):
    print(f"There isn't enough space! {all_people} people in a queue!")
    print(" ".join([str(i) for i in cabins]))

# if No more waiting people and No more free space
elif all_people == 0 and cabins.count(4) == len(cabins):
    print(" ".join([str(i) for i in cabins]))


