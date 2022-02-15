all_items = input().split(" ")
searched_products = input().split(" ")

inventory = {}
for idx in range(0, len(all_items), 2):
    key = all_items[idx]
    value = int(all_items[idx + 1])
    inventory[key] = value

for product in searched_products:
    if product in inventory:
        print(f"We have {inventory[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

