import itertools

names = input().split(", ")
chairs = int(input())

result = list(itertools.combinations(names, chairs))
for el in result:
    print(', '.join(el))

