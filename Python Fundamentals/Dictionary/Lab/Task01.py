bakery_items = input().split(" ")

bakery = {}

for idx in range(0, len(bakery_items), 2):
    key = bakery_items[idx]
    value = int(bakery_items[idx + 1])
    bakery[key] = value

print(bakery)