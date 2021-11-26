n = int(input())

for col in range(1, n + 1):
    for row in range(1, col + 1):
        print("*", end="")
    print()

for col in range(n - 1, 0, -1):
    for row in range(col, 0, -1):
        print("*", end="")
    print()