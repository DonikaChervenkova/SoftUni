rows, columns = [int(i) for i in input().split(", ")]

matrix = []
for _ in range(rows):
    line = [int(i) for i in input().split(", ")]
    matrix.append(line)

total_sum = 0
for row in range(rows):
    for col in range(columns):
        total_sum += matrix[row][col]

print(total_sum)
print(matrix)
