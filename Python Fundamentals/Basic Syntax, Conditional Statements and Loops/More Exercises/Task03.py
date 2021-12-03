year = int(input())

next_year = year + 1

while len(str(year)) != len(set(str(next_year))):
    next_year += 1

print(next_year)