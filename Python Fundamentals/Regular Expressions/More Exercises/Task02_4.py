import re

data = input()

total_income = 0
pattern = r"\%(?P<customer>[A-Z][a-z]+)\%[^\|\$%\.]*?\<(?P<product>\w+)\>[^\|\$%\.]*?\|(?P<count>[0-9]+)\|.*?(?P<price>[0-9]+\.?[0-9]+)\$"

while data != "end of shift":
    matches = re.finditer(pattern, data)
    if matches:
        for match in matches:
            line_info = match.groupdict()
            total_product_price = int(line_info['count']) * float(line_info['price'])
            total_income += total_product_price

            print(f"{line_info['customer']}: {line_info['product']} - {total_product_price:.2f}")

    data = input()

print(f"Total income: {total_income:.2f}")