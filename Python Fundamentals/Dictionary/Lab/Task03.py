products = {}

command = input()
while command != "statistics":
    command = command.split(": ")

    key = command[0]
    value = int(command[1])
    if key not in products:
        products[key] = 0
    products[key] += value

    command = input()
print("Products in stock:")
for k, v in products.items():
    print(f"- {k}: {v}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")