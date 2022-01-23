def first_letter_of_word(current_word):
    digits = []
    new_current_word = []
    for letter in current_word:
        if letter.isdigit():
            digits.append(letter)
        elif letter.isalpha():
            new_current_word.append(letter)
    first_letter = chr(int("".join(digits)))
    new_current_word.insert(0, first_letter)
    return new_current_word


def change_chars(new_current_word):
    new_current_word[1], new_current_word[-1] = new_current_word[-1], new_current_word[1]
    return new_current_word


def add_uncripted_word(new_current_word, new_message_list: list):
    new_current_word = "".join(new_current_word)
    new_message_list.append(new_current_word)
    return new_message_list


def organize_words(unsecret_message):
    unsecret_message = " ".join(unsecret_message)
    return unsecret_message


secret_message = input().split(" ")

new_message = []
for word in secret_message:

    new_word = first_letter_of_word(word)
    new_word = change_chars(new_word)
    new_message = add_uncripted_word(new_word, new_message)

new_message = organize_words(new_message)

print(new_message)


