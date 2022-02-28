sequence_of_strings = input().split(" ")

final_string = ""

for current_str in sequence_of_strings:
    final_string += len(current_str) * current_str

print(final_string)
