import re
command = input()
total_price = 0
while command != "end of shift":
    current_price = 0
    pattern = r'%([A-Z][a-z]+)%[^\|\$%\.]*?<(\w+)>[^\|\$%\.]*?\|(\d+)\|.*?(\d+\.?\d+)\$'
    if re.search(pattern, command):
        name, product, quantity, price = re.search(pattern, command).groups()
        current_price = int(quantity) * float(price)
        print(f'{name}: {product} - {current_price:.2f}')
        total_price += current_price
    command = input()
print(f'Total income: {total_price:.2f}')