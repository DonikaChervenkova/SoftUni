n = int(input())

for letter_1 in range(97, 97 + n):
    for letter_2 in range(97, 97 + n):
        for letter_3 in range(97, 97 + n):
            print(chr(letter_1)+chr(letter_2)+chr(letter_3))



