characters = input().split(", ")

answer = {}
for letter in characters:
    answer[letter] = ord(letter)

print(answer)