word = input()

list_of_indices_of_capital_letters = []

for index, letter in enumerate(word):
    if letter.isupper():

        list_of_indices_of_capital_letters.append(index)

print(list_of_indices_of_capital_letters)