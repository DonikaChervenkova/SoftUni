line_1 = [int(i) for i in input().split(" ")]
line_2 = [int(i) for i in input().split(" ")]
line_3 = [int(i) for i in input().split(" ")]
field = []

we_have_a_winner = False
this_row_won = False
this_col_won = False
this_diagonal_won = False
first_win = False
second_win = False

#  check row
for row in (line_1, line_2, line_3):
    for possition in range(0, 3):
        if row[0] == row[1] == row[2] and row[0] != 0:
            this_row_won = True
            if row[0] == 1:
                first_win = True
            else:
                second_win = True
            break

    if this_row_won:
        break

#  check for winning columns
for i in range(0, 3):
    for col in (line_1, line_2, line_3):
        if line_1[i] == line_2[i] == line_3[i] and line_1 != 0:
            this_col_won = True
            if line_1[i] == 1:
                first_win = True
            else:
                second_win = True
            break

    if this_col_won:
        break

# check for diagonal winners
if line_1[0] == line_2[1] == line_3[2] and line_1[0] != 0:
    this_diagonal_won = True
    if line_1[0] == 1:
        first_win = True
    elif line_1[0] == 2:
        second_win = True

if line_1[2] == line_2[1] == line_3[0] and line_1[2] != 0:
    this_diagonal_won = True
    if line_1[2] == 1:
        first_win = True
    elif line_1[2] == 2:
        second_win = True

if this_col_won or this_row_won or this_diagonal_won:
    if first_win:
        print("First player won")
    elif second_win:
        print("Second player won")
else:
    print("Draw!")

