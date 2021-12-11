divisor = int(input())
bound = int(input())
set_of_n = set()
for n in range(1, bound + 1):
    if n % divisor == 0:
        set_of_n.add(n)

print(max(set_of_n))
