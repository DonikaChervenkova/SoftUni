budget = float(input())
price_1kg_flour = float(input())

colored_eggs = 0

price_1pack_eggs = price_1kg_flour * 0.75
price_250ml_milk = (price_1kg_flour + (price_1kg_flour * 0.25)) / 4

price_1_bread = price_1pack_eggs + price_1kg_flour + price_250ml_milk

count_breads = int(budget // price_1_bread)

for current_bread in range(1, count_breads + 1):
    colored_eggs += 3

    if current_bread % 3 == 0:
        lost_colored_eggs = current_bread - 2
        colored_eggs -= lost_colored_eggs

money_left = budget - (count_breads * price_1_bread)
print(f"You made {count_breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
