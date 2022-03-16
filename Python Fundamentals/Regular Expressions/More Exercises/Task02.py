import re

line = input()

pattern = r'([^$%\.|]+)?%(?P<name>[A-Z][a-z]+)%([^$%\.|]+)?<(?P<product>\w+)>([^$%\.|]+)?\|(?P<count>\d+)\|([^$%\.|\d]+)?(?P<price>\d+(\.\d+)?)\$([^$%\.|]+)?'
income = 0
while line != 'end of shift':
    match = re.match(pattern, line)
    if match:
        data = match.groupdict()
        total_price = int(data['count']) * float(data['price'])
        print(f"{data['name']}: {data['product']} - {total_price:.2f}")
        income += total_price
    line = input()

print(f"Total income: {income:.2f}")