numbers = [int(i) for i in input().split()]
answer = list(filter(lambda x: x % 2 == 0, numbers))

print(answer)