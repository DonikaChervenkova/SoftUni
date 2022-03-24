command = input()
total_price_without_tax = 0
special = False

while True:
    if command == "special":
        special = True
        break
    elif command == "regular":
        break

    else:
        price = float(command)
        if price < 0:
            print("Invalid price!")
            command = input()
            continue
        else:
            total_price_without_tax += price

    command = input()

taxes = total_price_without_tax * 0.2
total_price_with_tax = total_price_without_tax + taxes

if special is True:
    total_price_with_tax -= (total_price_with_tax * 0.1)

if total_price_with_tax == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_tax:.2f}$")


