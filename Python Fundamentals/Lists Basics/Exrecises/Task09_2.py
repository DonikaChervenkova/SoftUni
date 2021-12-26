def check_for_enough_money(budjet_info, price_of_item):
    if budjet_info >= price_of_item:
        return True


def buy_item(budjet_info, price_of_item, list_new_prices, total_profit):
    budjet_info -= price_of_item
    new_price = (price_of_item + (price_of_item * 0.4))
    total_profit += (new_price - price_of_item)
    list_new_prices.append(new_price)
    return budjet_info, list_new_prices, total_profit


items = input().split("|")
budjet = float(input())

collection_new_prices = []
profit = 0

for current_item in items:
    current_item = current_item.split("->")
    type = current_item[0]
    price = float(current_item[1])

    if type == "Clothes":
        if price <= 50.00:
            if check_for_enough_money(budjet, price):
                budjet, collection_new_prices, profit = buy_item(budjet, price, collection_new_prices, profit)

    elif type == "Shoes":
        if price <= 35.00:
            if check_for_enough_money(budjet, price):
                budjet, collection_new_prices, profit = buy_item(budjet, price, collection_new_prices, profit)

    elif type == "Accessories":
        if price <= 20.50:
            if check_for_enough_money(budjet, price):
                budjet, collection_new_prices, profit = buy_item(budjet, price, collection_new_prices, profit)


print(" ".join([str(f"{i:.2f}") for i in collection_new_prices]))
print(f"Profit: {profit:.2f}")

if sum(collection_new_prices) + budjet >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
