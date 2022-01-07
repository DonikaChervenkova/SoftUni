char_1 = input()
char_2 = input()


def print_chars(first_char, second_char):
    all_chars = []
    for current_char in range(ord(first_char) + 1, ord(second_char)):
        all_chars.append(chr(current_char))

    answer = " ".join(all_chars)
    return answer


print(print_chars(char_1, char_2))