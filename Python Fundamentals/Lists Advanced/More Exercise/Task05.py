def find_dots_positions(field):
    all_dots = []
    for row in range(len(field)):
        for el in range(len(field[row])):
            tmp = []
            if field[row][el] == ".":
                tmp.append(row)
                tmp.append(el)
                all_dots.insert(0, tmp)

    return all_dots








n_row = int(input())

field = []
for i in range(n_row):
    current_row = input().split(" ")
    field.append(current_row)


all_dots_positions = find_dots_positions(field)
print(all_dots_positions)

