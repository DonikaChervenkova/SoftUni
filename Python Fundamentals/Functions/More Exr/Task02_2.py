from math import floor


def descartes(point1, point11, point2, point22):
    if abs(point1) + abs(point11) > abs(point2) + abs(point22):
        return f"({floor(point2)}, {floor(point22)})"
    else:
        return f"({floor(point1)}, {floor(point11)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

result = descartes(x1, y1, x2, y2)
print(result)