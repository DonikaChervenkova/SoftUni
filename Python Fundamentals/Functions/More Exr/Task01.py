data_type = input()
command = input()


def multiply_by_2(num):
    result = int(num) * 2
    return result


def multiply_by_other(num):
    result = float(num) * 1.5
    return f"{result:.2f}"


def change_string(str):
    result = "$" + str + "$"
    return result


functions ={
    "int": multiply_by_2,
    "real": multiply_by_other,
    "string": change_string
}

print(functions[data_type](command))