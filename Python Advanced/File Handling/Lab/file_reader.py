try:
    with open("numbers.txt") as my_file:
        print(sum([int(line) for line in my_file.readlines()]))
except FileNotFoundError:
    print("File was not found")