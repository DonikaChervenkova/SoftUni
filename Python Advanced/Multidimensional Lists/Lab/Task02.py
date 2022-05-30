rows = int(input())

matrix = []
for _ in range(rows):
    line = [int(i) for i in input().split(", ") if int(i) % 2 == 0]
    matrix.append(line)

print(matrix)