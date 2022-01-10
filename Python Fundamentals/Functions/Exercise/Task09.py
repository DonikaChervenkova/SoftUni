password = input()


def check_len(pword):
    if 6 <= len(pword) <= 10:
        return True
    else:
        return "Password must be between 6 and 10 characters"


def check_for_letter_and_digits(pword):
    pword_ok = True

    for i in pword:
        if i.isalpha():
            continue
        elif i.isdigit():
            continue
        else:
            pword_ok = False
            break

    if pword_ok is True:
        return True
    else:
        return "Password must consist only of letters and digits"


def check_count_digits(pword):
    count_digits = 0

    for i in pword:
        if i.isdigit():
            count_digits += 1

    if count_digits >= 2:
        return True
    else:
        return "Password must have at least 2 digits"


def all_checks(check_1, check_2, check_3):
    if check_1 is True and check_2 is True and check_3 is True:
        print("Password is valid")

    else:
        for current_check in (check_1, check_2, check_3):
            if current_check is not True:
                print(current_check)


all_checks(check_len(password), check_for_letter_and_digits(password), check_count_digits(password))