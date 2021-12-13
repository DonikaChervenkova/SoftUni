number = int(input())

for i in range(2, number):
    is_prime = True
    if number % i == 0:
        is_prime = False
        break

if is_prime and number > 1:
    print("True")
else:
    print("False")