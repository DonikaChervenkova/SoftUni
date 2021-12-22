def new_ordered_cards(frs_part, scd_part, all_cards):
    new_cards = []
    for idx in range(0, int(len(all_cards) / 2)):
        new_cards.append(frs_part[idx])
        new_cards.append(scd_part[idx])
    return new_cards


def split_cards(all_cards):
    middle = int(len(all_cards) / 2)
    part_one = all_cards[:middle]
    part_two = all_cards[middle:]
    return part_one, part_two


cards = input().split()
count_shuffle = int(input())

for current_shuffle in range(count_shuffle):
    first_part, second_part = split_cards(cards)

    cards = new_ordered_cards(first_part, second_part, cards)

print(cards)