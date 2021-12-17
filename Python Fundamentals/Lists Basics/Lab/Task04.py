n = int(input())
word = input()

all_strings = []
filtered_strings = []

for current_str in range(n):
    string = input()
    all_strings.append(string)

for item in all_strings:
    if word in item:
        filtered_strings.append(item)

print(all_strings)
print(filtered_strings)


