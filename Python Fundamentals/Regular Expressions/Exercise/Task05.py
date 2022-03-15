import re

total_price = 0
all_products = []

data = input()
while data != "Purchase":
    pattern = r"^>>(?P<product>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)\b"
    matches = re.finditer(pattern, data)
    for current_match in matches:
        all_info = current_match.groupdict()
        total_price += float(all_info['price']) * int(all_info['quantity'])
        all_products.append(all_info['product'])

    data = input()

print("Bought furniture:")
for items in all_products:
    print(items)
print(f"Total money spend: {total_price:.2f}")