all_notes = [0] * 11

command = input()

while command != "End":
    command = command.split("-")
    importance = int(command[0])
    current_note = command[1]

    all_notes[importance] = current_note

    command = input()

# sorted_notes = [i for i in all_notes if i != 0]

sorted_notes = list(filter(lambda x: x != 0, all_notes))
print(sorted_notes)