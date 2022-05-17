def sorting_cheeses(**products_collection):

    sorted_products = dict(sorted(products_collection.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    result = []
    for k, v in sorted_products.items():
        result.append(k)
        for num in sorted(v, reverse=True):
            result.append(num)
    return '\n'.join([str(el) for el in result])

