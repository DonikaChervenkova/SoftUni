factor = int(input())
count = int(input())

nums = list(map(lambda x: x * factor, range(1, count + 1)))

print(nums)
