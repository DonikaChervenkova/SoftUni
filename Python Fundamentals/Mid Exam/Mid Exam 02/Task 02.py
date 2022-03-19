numbers = [int(i) for i in input().split(" ")]

command = input()

while command != "end":
    command = command.split(" ")
    to_do = command[0]

    if to_do == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])
        numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]

    elif to_do == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])

        number_1 = numbers[index_1]
        number_2 = numbers[index_2]
        result = number_1 * number_2
        numbers[index_1] = result

    elif to_do == "decrease":
        decr_numbers = [(i - 1) for i in numbers]
        numbers = decr_numbers

    command = input()

print(", ".join([str(i) for i in numbers]))