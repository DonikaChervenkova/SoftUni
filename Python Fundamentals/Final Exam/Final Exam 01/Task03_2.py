all_pieces = {}
n = int(input())

for _ in range(n):
    piece, composer, key = input().split("|")

    # collect info
    if piece not in all_pieces:
        all_pieces[piece] = {}
        all_pieces[piece]['composer'] = composer
        all_pieces[piece]['key'] = key

command = input()
while command != "Stop":
    command = command.split("|")
    to_do = command[0]
    piece = command[1]

    if to_do == "Add":
        composer = command[2]
        key = command[3]
        if piece in all_pieces:
            print(f"{piece} is already in the collection!")
        else:
            all_pieces[piece] = {}
            all_pieces[piece]['composer'] = composer
            all_pieces[piece]['key'] = key
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif to_do == "Remove":
        if piece in all_pieces:
            del all_pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif to_do == "ChangeKey":
        new_key = command[2]
        if piece in all_pieces:
            all_pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

sorted_pieces = dict(sorted(all_pieces.items(), key=lambda kvp: (kvp[0], kvp[1]['composer'])))

for kvp in sorted_pieces.items():
    print(f"{kvp[0]} -> Composer: {kvp[1]['composer']}, Key: {kvp[1]['key']}")
