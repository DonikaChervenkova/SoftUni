import re

n = int(input())

pattern = r"\@\#(\#+)?([A-Z][a-zA-Z0-9]{4,}[A-Z])\@\#(\#+)?"
for _ in range(n):
    data = input()
    matches = re.finditer(pattern, data)
    we_have_match = bool([m.group(0) for m in matches])

    if we_have_match:
        product = "".join([m.group(2) for m in re.finditer(pattern, data)])
        pattern_find_numbers = r"\d"
        numbers = re.findall(pattern_find_numbers, product)

        product_group = None
        if numbers:
            product_group = "".join(numbers)
        else:
            product_group = "00"
        print(f"Product group: {product_group}")

    else:
        print("Invalid barcode")
