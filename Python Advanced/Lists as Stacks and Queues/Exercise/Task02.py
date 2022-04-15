stack = []
n = int(input())

for _ in range(n):
    query = input()

    if query == "2":
        if stack:
            stack.pop()
    elif query == "3":
        if stack:
            print(max(stack))
    elif query == "4":
        if stack:
            print(min(stack))
    else:
        query = query.split()
        stack.append(int(query[-1]))

stack = reversed(stack)
print(', '.join([str(i) for i in stack]))

