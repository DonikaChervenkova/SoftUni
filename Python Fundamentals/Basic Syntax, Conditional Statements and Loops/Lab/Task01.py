number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
my_set = set()

for number in (number_1, number_2, number_3):
    my_set.add(number)

print(max(my_set))