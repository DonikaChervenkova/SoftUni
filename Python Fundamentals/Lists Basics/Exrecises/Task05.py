cards = input().split(" ")
n = int(input())

middle = int(len(cards) / 2)

for current_shuffle in range(1, n + 1):
    shuffles_cards = []

    first_half = cards[:middle]
    second_half = cards[middle:]

    for i in range(int(len(cards) / 2)):
        shuffles_cards.append(first_half[i])
        shuffles_cards.append(second_half[i])

    cards = shuffles_cards

print(shuffles_cards)
