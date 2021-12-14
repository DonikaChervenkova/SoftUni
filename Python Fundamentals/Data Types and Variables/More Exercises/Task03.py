key = int(input())
n = int(input())
new_word = ""

for current_letter in range(1, n + 1):
    letter = input()
    new_word += chr(ord(letter) + key)

print(new_word)