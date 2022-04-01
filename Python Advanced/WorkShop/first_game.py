class FullColumnError(Exception):
    pass


def col_is_valid(current_col, size_cols):
    if 0 <= current_col < size_cols:
        return True
    return False


def row_is_valid(current_row, size_rows):
    if 0 <= current_row < size_rows:
        return True
    return False


def find_first_free_row(board, size_rows, col):
    for row in range(size_rows - 1, - 1, -1):
        if board[row][col] == 0:
            return row
    raise FullColumnError


def print_matrix(mtrx):
    for row in mtrx:
        print(row)


matrix = []

n_rows = 6
n_cols = 7
first_win = False
second_win = False

row_up = (-1, 0)

horizontal = {
    "left": (0, -1),
    "right": (0, 1)
}

vertical = {
    "up": (-1, 0),
    "down": (1, 0)
}

diagonal_1 = {
    "up_left": (-1, -1),
    "down_right": (1, 1)
}

diagonal_2 = {
    "up_right": (-1, 1),
    "down_left": (1, -1)
}

counter_turns = 1

# matrix = [[0 for _ in range(n_cols)] for row_num in range(n_rows)]
for _ in range(n_rows):
    matrix.append([int(el) for el in list('0' * n_cols)])

flat_matrix = [el for row in matrix for el in row]

while True:
    if flat_matrix.count(0) == 0:
        print("There is no free place. No winner.")
        break
    # player one
    if counter_turns % 2 != 0:
        try:
            player_col = (int(input("Player 1, please choose a column ")) - 1)

            if col_is_valid(player_col, n_cols):
                first_free_row = None
                try:
                    first_free_row = find_first_free_row(matrix, n_rows, player_col)
                except FullColumnError:
                    print("This column is full. Please choose another one.")
                    continue
                matrix[first_free_row][player_col] = 1
                # [print(r) for r in matrix]
                print_matrix(matrix)

                for directions in (horizontal, vertical, diagonal_1, diagonal_2):
                    connected_slots = 1
                    for direction in directions:
                        next_row = first_free_row + directions[direction][0]
                        next_col = player_col + directions[direction][1]
                        while col_is_valid(next_col, n_cols) and row_is_valid(next_row, n_rows):
                            if matrix[next_row][next_col] == 1:
                                connected_slots += 1
                                if connected_slots == 4:
                                    first_win = True
                                    print("The winner is player 1")
                                    break
                                next_row += directions[direction][0]
                                next_col += directions[direction][1]
                            else:
                                break
                        if first_win:
                            break
                    if first_win:
                        break
                if first_win:
                    break
            else:
                print(f"Invalid column. Please select a number between {1} and {n_cols}")
                continue

        except ValueError:
            print(f"Please select a number between {1} and {n_cols}")
            continue

    # player two
    else:
        try:
            player_col = (int(input("Player 2, please choose a column ")) - 1)
            if col_is_valid(player_col, n_cols):
                first_free_row = None
                try:
                    first_free_row = find_first_free_row(matrix, n_rows, player_col)
                except FullColumnError:
                    print("This column is full. Please choose another one.")
                    continue
                matrix[first_free_row][player_col] = 2
                # [print(r) for r in matrix]
                print_matrix(matrix)

                for directions in (horizontal, vertical, diagonal_1, diagonal_2):
                    connected_slots = 1
                    for direction in directions:
                        next_row = first_free_row + directions[direction][0]
                        next_col = player_col + directions[direction][1]
                        while col_is_valid(next_col, n_cols) and row_is_valid(next_row, n_rows):
                            if matrix[next_row][next_col] == 2:
                                connected_slots += 1
                                if connected_slots == 4:
                                    second_win = True
                                    print("The winner is player 2")
                                    break
                                next_row += directions[direction][0]
                                next_col += directions[direction][1]
                            else:
                                break
                        if second_win:
                            break
                    if second_win:
                        break
                if second_win:
                    break

            else:
                print(f"Invalid column. Please select a number between {1} and {n_cols}")
                continue

        except ValueError:
            print(f"Please select a number between {1} and {n_cols}")
            continue

    counter_turns += 1