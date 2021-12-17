n = int(input())

positives = []
negatives = []

for current_number in range(n):
    number = int(input())

    if number >= 0:
        positives.append(number)

    else:
        negatives.append(number)

count_positives = len(positives)
sum_negatives = sum(negatives)

print(positives)
print(negatives)
print(f"""Count of positives: {count_positives}
Sum of negatives: {sum_negatives}
""")