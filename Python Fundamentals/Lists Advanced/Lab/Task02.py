wagons = int(input())

train = []

for i in range(wagons):
    train.append(0)

command = input()

while command != "End":
    command = command.split(" ")
    to_do = command[0]

    if to_do == "add":
        people = int(command[1])
        train[-1] += people

    elif to_do == "insert":
        index = int(command[1])
        people = int(command[2])
        train[index] += people

    elif to_do == "leave":
        index = int(command[1])
        people = int(command[2])
        train[index] -= people

    command = input()

print(train)