product_type = input()
count_of_products = int(input())


def total_price(product, count):
    result = None
    if product == "coffee":
        result = 1.50 * count

    elif product == "water":
        result = 1.00 * count

    elif product == "coke":
        result = 1.40 * count

    elif product == "snacks":
        result = 2.00 * count

    return f"{result:.2f}"


print(total_price(product_type, count_of_products))
