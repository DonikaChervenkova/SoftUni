import string


def find_all_lines(file_path):
    with open("text.txt", "r") as file:
        all_lines = file.read().split("\n")
    return all_lines


def find_count_letters(current_line):
    count = 0
    for char in current_line:
        if char.isalpha():
            count += 1
    return count


def find_count_marks(current_line):
    count_marks = 0
    for mark in punctuation_marks:
        count_marks += line.count(mark)
    return count_marks


punctuation_marks = string.punctuation

lines = find_all_lines("text.txt")

for idx, line in enumerate(lines):
    count_letters = find_count_letters(line)
    count_marks = find_count_marks(line)

    new_line = f'Line {idx + 1}: ' + line + f' ({count_letters})({count_marks})'
    with open("output.txt", "a") as file:
        file.write(f"{new_line}\n")






