numbers = [int(i) for i in input().split(" ")]

command = input()

while command != "end":
    command = command.split(" ")
    to_do = command[0]

    if to_do == "exchange":
        index = int(command[1])
        if 0 <= index < len(numbers):
            left_part_of_nums = numbers[:index + 1]
            right_part_of_nums = numbers[index + 1:]
            numbers = right_part_of_nums + left_part_of_nums
        else:
            print("Invalid index")

    elif to_do == "max":
        kind_of_number = command[1]
        if kind_of_number == "even":
            even_numbers = [i for i in numbers if i % 2 == 0]
            if not even_numbers:
                print("No matches")
            else:
                max_even_number = max(even_numbers)
                all_indexes = [i for i, num in enumerate(numbers) if num == max_even_number]
                print(all_indexes[-1])

        elif kind_of_number == "odd":
            odd_numbers = [i for i in numbers if i % 2 != 0]
            if not odd_numbers:
                print("No matches")
            else:
                max_odd_number = max(odd_numbers)
                all_indexes = [i for i, num in enumerate(numbers) if num == max_odd_number]
                print(all_indexes[-1])

    elif to_do == "min":
        kind_of_number = command[1]
        if kind_of_number == "even":
            even_numbers = [i for i in numbers if i % 2 == 0]
            if not even_numbers:
                print("No matches")
            else:
                min_even_number = min(even_numbers)
                all_indexes = [i for i, num in enumerate(numbers) if num == min_even_number]
                print(all_indexes[-1])

        elif kind_of_number == "odd":
            odd_numbers = [i for i in numbers if i % 2 != 0]
            if not odd_numbers:
                print("No matches")
            else:
                min_odd_number = min(odd_numbers)
                all_indexes = [i for i, num in enumerate(numbers) if num == min_odd_number]
                print(all_indexes[-1])

    elif to_do == "first":
        count = int(command[1])
        kind_of_numbers = command[2]

        if count > len(numbers):
            print("Invalid count")

        else:
            if kind_of_numbers == "even":
                even_numbers = [i for i in numbers if i % 2 == 0]
                print(even_numbers[:count])

            elif kind_of_numbers == "odd":
                odd_numbers = [i for i in numbers if i % 2 != 0]
                print(odd_numbers[:count])

    elif to_do == "last":
        count = int(command[1])
        kind_of_numbers = command[2]

        if count > len(numbers):
            print("Invalid count")

        else:
            if kind_of_numbers == "even":
                even_numbers = [i for i in numbers if i % 2 == 0]
                print(even_numbers[-count:None])

            elif kind_of_numbers == "odd":
                odd_numbers = [i for i in numbers if i % 2 != 0]
                print(odd_numbers[-count:None])

    command = input()

print(numbers)