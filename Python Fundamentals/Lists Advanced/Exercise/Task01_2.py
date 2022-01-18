searched_word = input().split(", ")
txt = input().split(", ")
b = []
[b.append(i) for i in searched_word for word in txt if i in word if i not in b]

print(b)
