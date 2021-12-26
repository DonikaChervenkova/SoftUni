collection_of_items = input().split("|")
budget = float(input())
list_of_new_prices = []
profit = 0

for current_item in collection_of_items:
    current_item = current_item.split("->")

    type_of_item = current_item[0]
    price = float(current_item[1])

    deal = False

    if budget >= price:

        if type_of_item == "Clothes":
            if price <= 50.00:
                deal = True

        elif type_of_item == "Shoes":
            if price <= 35.00:
                deal = True

        elif type_of_item == "Accessories":
            if price <= 20.50:
                deal = True

        if deal is True:
            budget -= price
            new_price = price + (price * 0.4)
            list_of_new_prices.append(new_price)
            profit += (new_price - price)

    else:
        continue

print(" ".join([str(f"{i:.2f}") for i in list_of_new_prices]))

print(f"Profit: {profit:.2f}")

new_budget = budget + sum(list_of_new_prices)
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")