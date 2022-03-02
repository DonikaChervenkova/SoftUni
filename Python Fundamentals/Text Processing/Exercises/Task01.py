def check_len(c_user):
    if 3 <= len(c_user) <= 16:
        return True


def check_contains(c_user):
    all_good = True
    for letter in c_user:
        if letter.isdigit():
            continue
        elif letter.isalpha():
            continue
        elif letter in ("-", "_"):
            continue
        else:
            all_good = False
            break

    return all_good


usernames = input().split(", ")

valid_usernames = []

for current_user in usernames:
    first_check = check_len(current_user)
    second_check = check_contains(current_user)

    if first_check and second_check:
        valid_usernames.append(current_user)

print("\n".join(i for i in valid_usernames))

