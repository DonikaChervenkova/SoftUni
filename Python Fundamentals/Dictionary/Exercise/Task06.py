collection_of_products = {}

command = input()
while command != "buy":
    command = command.split(" ")
    current_product = command[0]
    current_price = float(command[1])
    current_quantity = int((command[2]))

    if current_product not in collection_of_products:
        collection_of_products[current_product] = {}
        collection_of_products[current_product]["quantity"] = 0

    collection_of_products[current_product]["price"] = current_price
    collection_of_products[current_product]["quantity"] += current_quantity

    command = input()

for current_dict in collection_of_products:
    total_price = collection_of_products[current_dict]["price"] * collection_of_products[current_dict]["quantity"]
    print(f"{current_dict} -> {total_price:.2f}")
