number = list(map(lambda x: int(x), list(input())))
number.sort(reverse=True)
max_num = "".join([str(i) for i in number])
print(max_num)