count_lost_fights = int(input())
price_helmet = float(input())
price_sword = float(input())
price_shield = float(input())
price_armor = float(input())

total_expenses = 0
count_breaks_of_shield = 0

for lost_fight in range(1, count_lost_fights + 1):

    if lost_fight % 2 == 0:
        total_expenses += price_helmet

    if lost_fight % 3 == 0:
        total_expenses += price_sword

        if lost_fight % 2 == 0:
            total_expenses += price_shield
            count_breaks_of_shield += 1

            if count_breaks_of_shield % 2 == 0:
                total_expenses += price_armor
print(f"Gladiator expenses: {total_expenses:.2f} aureus")

