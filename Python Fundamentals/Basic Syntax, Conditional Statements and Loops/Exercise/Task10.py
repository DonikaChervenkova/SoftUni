quantity = int(input())
days = int(input())

price_ornament_set = 2
price_tree_skirt = 5
price_tree_garlands = 3
price_tree_lights = 15

total_cost = 0
christmas_spirit = 0

for current_day in range(1, days + 1):

    if current_day % 11 == 0:
        quantity += 2

    if current_day % 10 == 0:
        total_cost += (price_tree_skirt + price_tree_garlands + price_tree_lights)
        christmas_spirit -= 20

        if current_day == days:
            christmas_spirit -= 30

    if current_day % 5 == 0:
        total_cost += (quantity * price_tree_lights)
        christmas_spirit += 17

        if current_day % 3 == 0:
            christmas_spirit += 30

    if current_day % 3 == 0:
        total_cost += (quantity * (price_tree_skirt + price_tree_garlands))
        christmas_spirit += 13

    if current_day % 2 == 0:
        total_cost += (price_ornament_set * quantity)
        christmas_spirit += 5

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")

