numbers = [int(i) for i in input().split(" ")]

winner = ""
winner_time = None
left_time = 0
right_time = 0

index_of_middle_line = len(numbers) // 2

left_racer = numbers[:index_of_middle_line]
right_racer = numbers[index_of_middle_line + 1:]
right_racer.reverse()

for i in left_racer:
    if i != 0:
        left_time += i

    else:
        left_time -= (left_time * 0.2)

for j in right_racer:
    if j != 0:
        right_time += j

    else:
        right_time -= (right_time * 0.2)

if left_time < right_time:
    winner = "left"
    winner_time = f"{left_time:.1f}"

else:
    winner = "right"
    winner_time = f"{right_time:.1f}"

print(f"The winner is {winner} with total time: {winner_time}")


