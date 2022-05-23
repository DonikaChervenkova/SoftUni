def even_odd(*data):
    result = []
    numbers = data[:-1]
    searched_kind = data[-1]
    if searched_kind == 'odd':
        result = [i for i in numbers if i % 2 != 0]
    elif searched_kind == 'even':
        result = [i for i in numbers if i % 2 == 0]
    return result
