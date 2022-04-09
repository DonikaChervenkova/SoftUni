text = input()
parentheses = []

for idx in range(len(text)):
    if text[idx] == "(":
        parentheses.append(idx)
    elif text[idx] == ")":
        start_idx = parentheses.pop()
        print(text[start_idx: idx + 1])