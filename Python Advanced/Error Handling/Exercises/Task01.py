numbers_dictionary = {}

key = input()
while key != "Search":
    try:
        number = int(input())
    except ValueError:
        print("The variable number must be an integer")
    else:
        numbers_dictionary[key] = number
    key = input()

searched_key = input()

while searched_key != "Remove":
    try:
        print(numbers_dictionary[searched_key])
    except KeyError:
        print('Number does not exist in dictionary')
    searched_key = input()

key_to_del = input()

while key_to_del != "End":
    try:
        del numbers_dictionary[key_to_del]
    except KeyError:
        print('Number does not exist in dictionary')
    key_to_del = input()

print(numbers_dictionary)
