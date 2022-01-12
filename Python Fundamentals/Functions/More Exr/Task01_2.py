data_type = input()
second_line = input()


def data_types(type, x):
    result = None
    if type == "int":
        result = int(x) * 2
    elif type == "real":
        result = f"{(float(x) * 1.5):.2f}"
    elif type == "string":
        result = f"${x}$"

    return result


print(data_types(data_type, second_line))