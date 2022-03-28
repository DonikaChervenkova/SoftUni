def do_substitute(txt, substr, subst):
    if substr in txt:
        new_txt = txt.replace(substr, subst)
        print(new_txt)
        return new_txt
    else:
        print("Nothing to replace!")
        return txt


def cut(txt, idx, l):
    end_idx = idx + l
    new_txt = text[:idx] + txt[end_idx:]
    return new_txt


def take_odd(txt):
    new_txt = txt[1::2]
    return new_txt


text = input()

command = input()
while command != "Done":
    command = command.split(" ")
    to_do = command[0]

    if to_do == "TakeOdd":
        text = take_odd(text)
        print(text)

    elif to_do == "Cut":
        index = int(command[1])
        length = int(command[2])
        text = cut(text, index, length)
        print(text)

    elif to_do == "Substitute":
        substring = command[1]
        substitute = command[2]
        text = do_substitute(text, substring, substitute)

    command = input()

print(f"Your password is: {text}")