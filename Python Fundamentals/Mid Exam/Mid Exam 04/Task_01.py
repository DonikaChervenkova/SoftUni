quantity_food = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
weight_of_pig = float(input()) * 1000

all_good = True

for day in range(1, 30 + 1):
    quantity_food -= 300

    if quantity_food <= 0:
        all_good = False
        break

    if day % 2 == 0:
        quantity_hay -= (quantity_food * 0.05)

    if day % 3 == 0:
        quantity_cover -= (weight_of_pig / 3)

    if quantity_hay <= 0 or quantity_cover <= 0:
        all_good = False
        break

if all_good is True:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food / 1000:.2f}, Hay: {quantity_hay / 1000:.2f},\
 Cover: {quantity_cover / 1000:.2f}.")

else:
    print("Merry must go to the pet store!")


