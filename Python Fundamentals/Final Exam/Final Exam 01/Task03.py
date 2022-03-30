all_pieces = {}

n = int(input())

for _ in range(n):
    info = input().split("|")
    piece = info[0]
    composer = info[1]
    key = info[2]
    # collect info
    all_pieces[piece] = [composer, key]

command = input()
while command != "Stop":
    command = command.split("|")
    to_do = command[0]
    piece = command[1]

    if to_do == "Add":
        new_composer = command[2]
        new_key = command[3]
        if piece in all_pieces:
            print(f"{piece} is already in the collection!")
        else:
            all_pieces[piece] = [new_composer, new_key]
            print(f"{piece} by {new_composer} in {new_key} added to the collection!")

    elif to_do == "Remove":
        if piece not in all_pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        elif piece in all_pieces:
            del all_pieces[piece]
            print(f"Successfully removed {piece}!")

    elif to_do == "ChangeKey":
        new_key = command[2]
        if piece in all_pieces:
            all_pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

sorted_all_pieces = dict(sorted(all_pieces.items(),key=lambda x: (x[0],x[1][0])))

for piece in sorted_all_pieces:
    print(f"{piece} -> Composer: {sorted_all_pieces[piece][0]}, Key: {sorted_all_pieces[piece][1]}")