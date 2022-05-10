def find_even_lines(file_path):
    with open(file_path) as file:
        all_lines = file.read().split("\n")
        even_lines_of_file = [line for idx, line in enumerate(all_lines) if idx % 2 == 0]
    return even_lines_of_file


characters = ["-", ",", ".", "!", "?"]

even_lines = find_even_lines("text.txt")

for line in even_lines:
    for char in characters:
        line = line.replace(char, "@")
    print(' '.join(line.split()[::-1]))