expression = input()

stack = []
balanced = True
pairs = {
    '(': ')',
    '[': ']',
    '{': '}'
}
for el in expression:
    if el in '{[(':
        stack.append(el)
    else:
        if len(stack) == 0:
            balanced = False
            break
        last_opening_bracket = stack.pop()
        if pairs[last_opening_bracket] != el:
            balanced = False
            break

if balanced and len(stack) == 0:
    print("YES")
else:
    print("NO")
